import json
from os.path import expanduser, curdir, abspath

home = abspath(curdir)

path_to_strategy = home+"\strategy.json"
path_to_creds = home+"\creds.txt"
path_to_env = home+"\.env"
path_to_config = home+'\config.json'
selenium_driver_path = home+"\chromedriver.exe"
path_to_winers = home+"\winners.txt"
path_to_log = home+"\log.txt"
strategies = ["standart", "only_quests", "only_wins"]

with open(path_to_config, "r") as read_file:
    data = json.load(read_file)
TOKEN = data["token"]
ADMIN_ID = data["admin_id"]

