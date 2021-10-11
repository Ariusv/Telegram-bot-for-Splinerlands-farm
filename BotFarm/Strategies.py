import json

import requests

from BotFarm.Supportfuncs import *
from config import *
import time

class Strategy:
    def __init__(self, type, dec, interapted, threads, selected_bots, local_base_extend=True):
        self.type = type
        self.dec = dec
        self.local_base_extend = local_base_extend
        self.interapted = interapted
        self.selected_bots = selected_bots
        self.threads = threads

    def bot_act(self, bot, shell):
        edit_env(bot, path_to_env)
        bot.battle_count += 1
        shell.start()
        time.sleep(2)

    def timer(self):
        time.sleep(self.dec)

    def start(self, bot, shell, log):
            if self.type == strategies[2]:
                bot.quest_priority = "false"
            info = log.log_bot_start(bot)
            self.bot_act(bot, shell)
            return info

    def winner_check(self, bot):
            winner=self.winner_check_(bot)
            if winner == bot.game_login:
                bot.wins += 1
                return bot.game_login + " won!"
            else:
                self.add_winner(winner)
                return bot.game_login + " lose! Winner: " + winner

    def add_winner(self, winner):
        if self.local_base_extend == True:
            if winner!="DRAW":
                with open(path_to_winers, "a") as file:
                    file.write(" " + winner)

    def clear_winners(self):
        with open(path_to_winers, "w") as file:
            file.write("")

    def winner_check_(self, bot):
        try:
            params = {'key': 'value'}
            response_win = requests.get(url="https://api.steemmonsters.io/battle/history?player=" + bot.game_login,
                                    params=params).json()
            winner_json =response_win["battles"][0]
            winner = winner_json["winner"]
            return winner
        except:
            return "DRAW"

    def dump_strategy(self ):
        data = {
            "type": self.type,
            "dec": self.dec,
            "interapted": self.interapted,
            "threads": self.threads,
            "selected_bots": self.selected_bots
        }
        with open(path_to_strategy, "w") as write_file:
            json.dump(data, write_file)

    def load_strategy(self ):
        with open(path_to_strategy, "r") as read_file:
            data = json.load(read_file)
        self.dec= data["dec"]
        self.type = data["type"]
        self.interapted = data["interapted"]
        self.threads = data["threads"]
        self.selected_bots = data["selected_bots"]

