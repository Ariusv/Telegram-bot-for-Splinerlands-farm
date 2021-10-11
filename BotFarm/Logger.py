from BotFarm.Bots import *

class LogAdministrator:

    def clean_log(self):
        with open(path_to_log, "w") as file:
            file.write("")

    def log_start(self):
        now = datetime.datetime.now()
        str_ = str(now.date())+"  "+str(now.time()).split(".")[0]+" START "+"\n\n"
        with open(path_to_log, "a") as file:
            file.write(str_ + " \n")
        return str_
    def log_bot_start(self, bot):
        try:
            now = datetime.datetime.now()
            str_ = str(now.time()).split(".")[0] + " bot: " + bot.game_login + " battles: " + str(bot.battle_count)+" victories: " + str(bot.wins) +" "+bot.quest_name+": "+bot.quest_status + " rating: "+str(bot.rating) + " decs: " + str(bot.decs)
            with open(path_to_log, "a") as file:
                file.write(str_ + " \n")
            return str_
        except:
            return "Log error"


    def log_winner(self, info):
        now = datetime.datetime.now()
        str_ = str(now.time()).split(".")[0] + " "+info
        with open(path_to_log, "a") as file:
            file.write(str_ + " \n")
        return str_

    def log_pause(self):
        now = datetime.datetime.now()
        str_ = str(now.date())+"  "+str(now.time()).split(".")[0] + " PAUSE"
        with open(path_to_log, "a") as file:
            file.write(str_ + " \n")
        return str_

    def log_stop(self):
        now = datetime.datetime.now()
        str_ = str(now.date())+"  "+str(now.time()).split(".")[0] + " STOP"
        with open(path_to_log, "a") as file:
            file.write(str_ + " \n")
        return str_

    def log_withdraw(self, decs, login):
        now = datetime.datetime.now()
        str_ = str(now.time()).split(".")[0] + " Withdrew "+str(decs)+" with"+login
        with open(path_to_log, "a") as file:
            file.write(str_ + " \n")
        return str_

    def skip_quest(self, login):
        now = datetime.datetime.now()
        str_ = str(now.time()).split(".")[0] + " Quest was skipped "+login
        with open(path_to_log, "a") as file:
            file.write(str_ + " \n")
        return str_

    def change_strategy(self, strategy):
        now = datetime.datetime.now()
        str_ = str(now.time()).split(".")[0] + " Strategy was changed: " + str(strategy.type) + " " + str(strategy.dec)+" "+str(strategy.threads)
        with open(path_to_log, "a") as file:
            file.write(str_ + " \n")
        return str_


