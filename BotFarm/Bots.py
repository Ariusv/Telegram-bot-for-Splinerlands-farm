import asyncio

from BotFarm.Processes import *
from BotFarm.Selenium_extension import BotExtension
from BotFarm.Supportfuncs import *
from BotFarm.Selenium_extension import *
from config import *
import datetime
import time
import requests
import json
from BotFarm.Logger import LogAdministrator

class Bot:
    def __init__(self, data):
        self.game_login = data[0]
        self.email = data[1]
        self.p_key = data[2]
        self.a_key = data[3].replace("\n", "")
        self.battle_count = 0
        self.wins = 0
        self.decs = ""
        self.credits = ""
        self.power = ""
        self.rating = ""
        self.rate = ""
        self.quest_name = ""
        self.quest_status = ""
        self.quest_priority = "false"
        self.quest_created = ""
        self.quest_claim_date = ""


    def bot_creds_to_string(self):
        str = "Login: "+self.game_login + "\n " + "Email: "+self.email + "\n " + "Posting key: "+self.p_key + "\n " + "Active key: "+self.a_key+ "\n"
        return str
    def bot_data_to_string(self):
        string_ = "Login: "+self.game_login + "\n" +"Decs: "+ str(self.decs) + "\n" +"Credits: "+ str(self.credits) + "\n" +"Power: "+ str(self.power) + "\n" +"Rating: "+ str(self.rating)+ "\n"+ "-"*45+"\nQuest: "+ str(self.quest_name)+" "+self.quest_status+"\n"+"created: "+self.quest_created+"\nclaim date: "+self.quest_claim_date+"\n"+"-"*45+"\n"
        return string_

class BotAdministrator:
    def __init__(self, bots, strategy):
        self.bots = bots
        self.strategy = strategy


    def bots_creds_to_string(self):
        str = ""
        for bot in self.bots:
            str += bot.bot_creds_to_string()+"\n"
        return str

    def bots_data_to_string(self):
        string_ = ""
        for bot in self.bots:
            string_ += bot.bot_data_to_string()+"\n"
        return string_

    def run(self, loger):
        log = loger
        shell = ProcessAdministrator()

        while True:

            time.sleep(1)
            self.strategy.load_strategy()

            if not self.strategy.interapted:
                time.sleep(1)
                p = self.strategy.threads
                print(self.strategy.threads)
                bots = []

                if self.strategy.type == strategies[1]:
                    self.check_all()


                for bot in self.bots:
                    if self.strategy.type == strategies[1]:
                        if bot.quest_claim_date == " | ":
                            if bot.game_login in self.strategy.selected_bots:
                                print(bot.game_login)
                                bots.append(bot)
                    else:
                        if bot.game_login in self.strategy.selected_bots:
                            bots.append(bot)

                n = len(bots)
                if n==0:
                    bots = self.bots

                l = n // p
                d = n % p
                print(l)
                print(d)
                print(p)
                print(n)
                ind = 0
                for i in range(l):

                    self.strategy.load_strategy()
                    if self.strategy.interapted:
                        break

                    bots_processes = []

                    for j in range(ind, ind+p):
                        bot = bots[j]
                        self.check(bot)
                        shell = ProcessAdministrator()
                        self.strategy.start(bot, shell, log)
                        bots_processes.append(shell.pid)

                    self.strategy.timer()

                    #for pid in bots_processes:
                        #shell.kill(pid)

                    for j in range(ind, ind + p):
                        bot = bots[j]
                        victory_info = self.strategy.winner_check(bot)
                        log.log_winner(victory_info)
                    ind = ind + p

                if d != 0:
                    self.strategy.load_strategy()
                    bots_processes = []
                    for j in range(ind, ind + d):

                        if self.strategy.interapted:
                            break

                        bot = bots[j]
                        self.check(bot)
                        self.strategy.start(bot, shell, log)
                        bots_processes.append(shell.pid)

                    if not self.strategy.interapted:
                        self.strategy.timer()

                    #for pid in bots_processes:
                        #shell.kill(pid)

                    for j in range(ind, ind + d):

                        if self.strategy.interapted:
                            break

                        bot = bots[j]
                        victory_info = self.strategy.winner_check(bot)
                        log.log_winner(victory_info)


    def check_all_with_selenium(self):
        for bot in self.bots:
            browser = webdriver.Chrome(selenium_driver_path)
            checker = BotExtension(bot, browser)
            checker.check()

    def check_all(self):
        for bot in self.bots:
            self.check(bot)

    def withdraw_on_wallet(self, bot):
        browser = webdriver.Chrome(selenium_driver_path)
        withdrawer = BotExtension(bot, browser)
        decs = withdrawer.withdraw_on_wallet()
        return decs

    def withdraw_to_player(self, bot, player):
        browser = webdriver.Chrome(selenium_driver_path)
        checker = BotExtension(bot, browser)
        decs = checker.withdraw_to_player(player, True)
        return decs
    def check(self, bot):
        try:
            params = {'key': 'value'}
            response_dec = requests.get(url="https://api.splinterlands.io/players/balances?username=" + bot.game_login,
                                params=params).json()
            response_rating = requests.get(url="https://api.splinterlands.io/players/details?name=" + bot.game_login,
                                params=params).json()
            response_quest = requests.get(url="https://api.splinterlands.io/players/quests?username=" + bot.game_login,
                                params=params).json()
            balance = ""
            credits = ""
            for dic in response_dec:
                if dic["token"]=="DEC":
                    balance = dic["balance"]
                if dic["token"]=="CREDITS":
                    credits = dic["balance"]


            bot.decs = balance
            if credits == "":
                bot.credits = 0
            else:
                bot.credits = credits
            bot.rating = response_rating["rating"]
            bot.power = response_rating["collection_power"]
            bot.quest_name = response_quest[0]["name"]
            bot.quest_status = str(response_quest[0]["total_items"]) + ":"+ str(response_quest[0]["completed_items"])
            if response_quest[0]["completed_items"] == 5:
                bot.quest_priority = "false"
            else:
                bot.quest_priority = "true"

            quest_created = str(response_quest[0]["created_date"])
            bot.quest_created = quest_created[5:10]+" | "+quest_created[11:16]

            claim_date = str(response_quest[0]["claim_date"])
            bot.quest_claim_date = claim_date[5:10]+" | "+claim_date[11:16]
        except:
            print("CHECK EXCEPTION!!!")

    def skip_quest(self, bot):
        browser = webdriver.Chrome(selenium_driver_path)
        checker = BotExtension(bot, browser)
        checker.new_quest()

    def bot_add(self, bot):
        self.bots.append(bot)

    def bot_remove(self, login):
        for bot in self.bots:
            if bot.game_login =="login":
                self.bots.remove(bot)

    def send_cards_to_player(self,bot, login):
        browser = webdriver.Chrome(selenium_driver_path)
        checker = BotExtension(bot, browser)
        return checker.send_cards_to_player(login)

