import asyncio

import BotFarm.Bots


def read_bots_from_file(path):
    with open(path, "r") as file:
        accounts_creds = file.readlines()
    bots = []
    for data in accounts_creds:
        data = data.split()
        bot = BotFarm.Bots.Bot(data)
        bots.append(bot)
    return bots

def edit_env(bot, path):
    file = open(path, "w")
    file.write("QUEST_PRIORITY="+bot.quest_priority+"\nACCOUNT="+bot.game_login+"\nPASSWORD="+bot.p_key)
    file.close()

def concat_winners_files(pathes):
    str_=""
    for path in pathes:
        with open(path, "r") as file:
            str_ += file.read()
    print(str_)
    winners = set(str_.replace("\\n", "").split(" "))

    with open(pathes[0], "w") as file:
        for winner in winners:
            file.write(" " + winner)

def run_(farm, loger):
    farm.run( loger)

