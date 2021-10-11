from aiogram.types import CallbackQuery
import threading
from BotFarm.Bots import BotAdministrator
from BotFarm.Logger import LogAdministrator
from BotFarm.States import States
from BotFarm.Buttons import *
from BotFarm.Strategies import Strategy
from BotFarm.loader import bot, dp, storage
from config import *
from BotFarm.Supportfuncs import *
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import  types
import time
import asyncio
import script


@dp.message_handler(commands=['start'],state='*')
async def start_command(message: types.Message, state:FSMContext):
    if message.from_user.id==ADMIN_ID:
        await message.answer(text="Bot is starting...")
        async with state.proxy() as data:
            data["strategy"] = "standart"
            data["threads"] = 2
            data["time"] = 10
            data["selected_bots"] = [bot.game_login for bot in read_bots_from_file(path_to_creds)]
        await message.answer(text="Hi!\nThe bot farm reloaded",  reply_markup=menu_buttons_start)
    else:
        await message.answer("Hah")

@dp.message_handler(text="Set a strategy",state='*')
async def choose_strategy(message: types.Message, state:FSMContext):
    await message.answer("Strategies:", reply_markup=strategy_buttons)
    await States.Choose_strategy.set()

@dp.callback_query_handler(state=States.Choose_strategy)
async def choose_strategy(callback_query: types.CallbackQuery, state:FSMContext):
    await bot.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        if str(callback_query.data) == "only_quests":
            data["strategy"]="only_quests"
        elif str(callback_query.data) == "only_wins":
            data["strategy"]="only_wins"
        elif str(callback_query.data) == "standart":
            data["strategy"] = "standart"
        else:
            data["strategy"] = "standart"
    data = await state.get_data()
    await bot.send_message(callback_query.from_user.id, "Strategy: "+data.get("strategy"))
    await bot.send_message(callback_query.from_user.id, "Count of threads:")
    await States.Choose_count_of_threads.set()

@dp.message_handler(state=States.Choose_count_of_threads)
async def choose_threads(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        try:
            threads = int(message.text)
            if threads > 0 and threads < 5:
                data["threads"] = threads
                await message.answer("Threads: " + str(data.get("threads")))
                await message.answer("Time:")
                await States.Choose_time.set()
            else:
                await message.answer("Wrong count!")
        except:
            await message.answer("Wrong count!")



@dp.message_handler(state=States.Choose_time)
async def choose_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            time = int(message.text)
            if time > 0:
                data["time"] = time
                await message.answer("Time: " + str(data.get("time")))
                await message.answer("Enter bot logins or write \"all\":")
                await States.Choose_bots.set()
            else:
                await message.answer("Wrong time!")
        except:
            await message.answer("Wrong time!")

@dp.message_handler(state=States.Choose_bots)
async def choose_bots(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        logins = message.text.replace(",", "").split(" ")
        if logins[0] == "all":
            data["selected_bots"] = script.bot_logins
            await message.answer("Choosed all bots")
        else:
            bots = []
            for bot in script.farm.bots:
                if bot.game_login in logins:
                    bots.append(bot.game_login)
                    await message.answer("Choose "+bot.game_login)
            data["selected_bots"] = bots

        script.log.change_strategy(Strategy(data["strategy"], data["time"], False, data["threads"], data["selected_bots"]))
        await state.reset_state(with_data=False)

@dp.message_handler(text="Start", state=None)
async def init_farm(message: types.Message, state:FSMContext):
    script.log.log_start()
    async with state.proxy() as data:
        strategy = Strategy(data["strategy"], data["time"], False, data["threads"], data["selected_bots"])

        strategy.dump_strategy()

    await message.answer("The bot farm run!", reply_markup=menu_buttons_start)

@dp.message_handler(text="Stop", state=None)
async def stop_farm(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        strategy = Strategy(data["strategy"], data["time"], True, data["threads"], data["selected_bots"])
        strategy.dump_strategy()
    script.log.log_stop()
    await message.answer("The bot farm is stopping!", reply_markup=menu_buttons_stop)
    await state.reset_state(with_data=False)

@dp.message_handler(text="Send cards", state=None)
async def send_cards(message: types.Message, state:FSMContext):
    await message.answer("Enter player name:")
    await States.Send_cards_choose_player.set()

@dp.message_handler(state=States.Send_cards_choose_player)
async def send_cards(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data["player_for_sending_cards"] = message.text
        await message.answer("Choosed "+data["player_for_sending_cards"])
    await message.answer("Send:", reply_markup=send_cards_buttons)
    await States.Send_cards.set()

@dp.callback_query_handler(state=States.Send_cards)
async def send_cards(callback_query: types.CallbackQuery, state:FSMContext):
    await bot.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        if str(callback_query.data) == "send_all_cards":
            await bot.send_message(callback_query.from_user.id, "Please wait...")
            for _ in script.farm.bots:
                result_string = script.farm.send_cards_to_player(_, data["player_for_sending_cards"])
                await bot.send_message(callback_query.from_user.id, result_string)
            await state.reset_state(with_data=False)
        elif str(callback_query.data) == "send_some_cards":
            await bot.send_message(callback_query.from_user.id, "Enter logins:")
            await States.Send_cards_from_some_bots.set()

@dp.message_handler( state=States.Send_cards_from_some_bots)
async def send_cards_from_some_bots(message: types.Message, state:FSMContext):
    await message.answer("Please wait...")
    logins = message.text.replace(",", "").split(" ")
    for bot in script.farm.bots:
        if bot.game_login in logins:
            data = await state.get_data()
            result_string = script.farm.send_cards_to_player(bot, data["player_for_sending_cards"])
            await message.answer(result_string)
    await state.reset_state(with_data=False)

@dp.callback_query_handler(state=States.Check_bots)
async def check_strategy(callback_query: types.CallbackQuery, state:FSMContext):
    await bot.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        if str(callback_query.data) == "check_all":
            await bot.send_message(callback_query.from_user.id, "Please wait...")
            script.farm.check_all()
            for _ in script.farm.bots:
                await bot.send_message(callback_query.from_user.id, _.bot_data_to_string())
            try:
                await bot.send_message(callback_query.from_user.id,
                                       "Decs: "+str(sum([_.decs for _ in script.farm.bots])))
            except:
                await bot.send_message(callback_query.from_user.id, "Decs: Error" )
            try:
                await bot.send_message(callback_query.from_user.id,
                                       "Credits: "+str(sum([_.credits for _ in script.farm.bots])))
            except:
                await bot.send_message(callback_query.from_user.id, "Credits: Error" )
            try:
                await bot.send_message(callback_query.from_user.id, "Power: "+ str(sum([_.power for _ in script.farm.bots])))
            except:
                await bot.send_message(callback_query.from_user.id, "Power: Error")
            await state.reset_state(with_data=False)
        elif str(callback_query.data) == "check_some_bots":
            await bot.send_message(callback_query.from_user.id, "Enter logins:")
            await States.Check_some_bots.set()
        elif str(callback_query.data) == "send_log_file":
            with open(path_to_log, 'rb') as file:
                await bot.send_document(chat_id=callback_query.from_user.id, document=file)
                await state.reset_state(with_data=False)

@dp.message_handler( state=States.Check_some_bots)
async def check_some_bots(message: types.Message, state:FSMContext):
    await message.answer("Please wait...")
    logins = message.text.replace(",", "").split(" ")
    for bot in script.farm.bots:
        if bot.game_login in logins:
            script.farm.check(bot)
            await message.answer(bot.bot_data_to_string())
    await state.reset_state(with_data=False)

@dp.message_handler(text="Check", state=None)
async def check_bots(message: types.Message, state:FSMContext):
    await message.answer("Check:", reply_markup=check_buttons)
    await States.Check_bots.set()

@dp.message_handler(text="Withdraw decs", state=None)
async def withdraw_decs(message: types.Message, state:FSMContext):
    await message.answer("Choose a type:", reply_markup=withdraw_player_wallet_buttons)
    await States.Change_type_withdraw.set()


@dp.callback_query_handler(state=States.Change_type_withdraw)
async def withdraw_decs(callback_query: types.CallbackQuery, state:FSMContext):
    await bot.answer_callback_query(callback_query.id)

    async with state.proxy() as data:
        if str(callback_query.data) == "withdraw_to_player":
            await bot.send_message(callback_query.from_user.id, "Enter a player login to withdraw decs:")
            await States.Enter_player_to_withdraw.set()
        elif str(callback_query.data) == "withdraw_on_wallet":
            data["target_to_withdraw"] = "wallet"
            await  bot.send_message(callback_query.from_user.id,"Withdraw:", reply_markup=withdraw_buttons)
            await States.Withdraw_decs.set()

@dp.message_handler(state=States.Enter_player_to_withdraw)
async def withdraw_decs(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        player = message.text
        data["target_to_withdraw"] = player
        await  message.answer("Withdraw:", reply_markup=withdraw_buttons)
        await States.Withdraw_decs.set()
@dp.callback_query_handler(state=States.Withdraw_decs)
async def choose_withdraw(callback_query: types.CallbackQuery, state:FSMContext):
    await bot.answer_callback_query(callback_query.id)
    async with state.proxy() as data:
        if str(callback_query.data) == "withdraw_all_decs":
            await bot.send_message(callback_query.from_user.id, "Please, wait...")
            sum = 0
            for _ in script.farm.bots:
                if data["target_to_withdraw"] == "wallet":
                    decs = script.farm.withdraw_on_wallet(_)
                else:
                    decs = script.farm.withdraw_to_player(_, data["target_to_withdraw"])
                sum+=decs
                script.log.log_withdraw(decs, _.game_login)
                await bot.send_message(callback_query.from_user.id, _.game_login + ":  " + str(decs))
            await bot.send_message(callback_query.from_user.id, "Withdrew " + str(sum))
            await state.reset_state(with_data=False)
        elif str(callback_query.data) == "withdraw_some_decs":
            await bot.send_message(callback_query.from_user.id, "Enter logins:")
            await States.Withdraw_decs_with_some_bots.set()

@dp.message_handler( state=States.Withdraw_decs_with_some_bots)
async def check_some_bots(message: types.Message, state:FSMContext):
    await message.answer("Please wait...")
    data = await state.get_data()
    logins = message.text.replace(",", "").split(" ")
    sum = 0
    for bot in script.farm.bots:
        if bot.game_login in logins:
            if data["target_to_withdraw"] == "wallet":
                decs = script.farm.withdraw_on_wallet(bot)
            else:
                decs = script.farm.withdraw_to_player(bot, data["target_to_withdraw"])
            sum+=decs
            script.log.log_withdraw(decs, bot.game_login)
            await message.answer(bot.game_login +":  "+ str(decs))
    await message.answer("Withdrew " + str(sum))
    await state.reset_state(with_data=False)

@dp.message_handler(text="Skip quests", state=None)
async def skip_quests(message: types.Message, state:FSMContext):
    await message.answer("Enter logins:")
    await States.Skip_quest.set()

@dp.message_handler( state=States.Skip_quest)
async def skip_quests(message: types.Message, state:FSMContext):
    await message.answer("Please wait...")
    logins = message.text.replace(",", "").split(" ")
    for bot in script.farm.bots:
        if bot.game_login in logins:
            script.farm.skip_quest(bot)
            script.log.skip_quest(bot.game_login)
            await message.answer(bot.game_login+": "+"quest was skipped")

    await state.reset_state(with_data=False)
