
### ENG
Read this in other languages: [Ukrainian](https://github.com/Ariusv/Telegram-bot-for-Splinerlands-farm/blob/main/README-UA.md)
# A Telegram bot for managing accounts in Splinterlands
It's an add-on for [the alfficcadenti bot](https://github.com/alfficcadenti/splinterlands-bot)

## Donation
I will be grateful for possible donation)
* BSC - 0xB82D7f7092145A587151DE7329183D7561207d2D
* ETHEREUM - 0xB82D7f7092145A587151DE7329183D7561207d2D

## Installation
You must install  [Python](https://www.python.org/downloads/) and [NodeJS](https://nodejs.org/it/download/) first.
After that, you need to download [chromedriver](https://chromedriver.chromium.org/downloads) to the bot folder and run:
* npm install
* pip install selenium
* pip install psutil
* pip install requests
* pip install aiogram

Enter Splinterlands account credentials in the format (one account - one line) in creds.txt:

* login email posting_key active_key
* login email posting_key active_key
* ...


And then include in config.json:

* "token": "token of your [bot](https://core.telegram.org/bots) in quotes"
* "admin_id": your [chat_id](https://telegram.me/GetMyIdBot_bot) without quotes


Example: 
{"token": "738309:4mfeo94ckdmv493mdk", "admin_id":1729304736 }

Сopy the newHistory.json local battle database to "data".

Run script.py. In the initial configuration, the bot will run in two threads with an interval of 180 seconds in the standard battle strategy.

#### !!!

To work with the bot, it is advisable to install the IDE [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/) because there is an unresolved issue with the termination of processes. If you run in the console or standard IDE, then after closing the program you need to manually terminate the Python process in the task manager.

## Functionality

* /start - restart the bot
![](/images/1.png)
* Stop - stop the farm. You should wait a while for the running accounts to complete the game.
![](/images/2.jpg)
* Check - It is possible to view the log file, get information about all or some accounts.
![](/images/3.jpg)
![](/images/4.jpg)
![](/images/5.png)
* Set a strategy - choosing a game strategy for accounts. It is desirable to stop the bot first before choosing a strategy.
  *  Standart - accounts first complete quests and then play to win Після завершення квесту гратиме "найкращими" комбінаціями.
  *  Quests - only accounts play that have not completed quests.
  *  Wins - accounts will not complete quests.
* Threads - a number of threads.
* Time - time in seconds between games.
* You can also choose which accounts will play.
![](/images/6.jpg)
![](/images/7.png)
* Start - start with the chosen strategy
* Withdraw decs - sending decs to the BSC wallet or player from all or some accounts. The wallet must be saved in each account.
* Send cards - sending cards to player from all or some accounts.
* Skip quests.
