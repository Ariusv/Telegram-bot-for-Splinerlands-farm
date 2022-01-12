from BotFarm.Bots import BotAdministrator
from BotFarm.Strategies import *
from config import *
from BotFarm.Supportfuncs import *
from BotFarm.Logger import LogAdministrator
from aiogram.dispatcher import FSMContext
from BotFarm.loader import bot, dp, storage

import multiprocessing

async def on_shutdown(dp):

    await bot.close()
    await storage.close()

async def send_to_admin(dp):
    await bot.send_message(chat_id=ADMIN_ID, text="Bot is working!")


bots_ = read_bots_from_file(path_to_creds)
bot_logins = [bot.game_login for bot in bots_]
strategy = Strategy("standart", 180, False, 3, bot_logins)
strategy.dump_strategy()
farm = BotAdministrator(bots_, strategy)
log = LogAdministrator()
if __name__ == "__main__":
    from BotFarm.handlers import *
    from aiogram.utils import executor

    log.clean_log()
    log.log_start()

    multiprocessing.Process(target=run_, args=((farm, log,))).start()


    executor.start_polling(dp, skip_updates=False, on_shutdown=on_shutdown)




#concat_winners_files(["winners1.txt", "winners2.txt"])










