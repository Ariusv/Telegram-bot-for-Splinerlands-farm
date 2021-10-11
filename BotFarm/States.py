from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    Choose_strategy = State()
    Start = State()
    Choose_count_of_threads = State()
    Choose_time = State()
    Choose_bots = State()
    Check_bots = State()
    Check_some_bots = State()
    Change_type_withdraw = State()
    Enter_player_to_withdraw = State()
    Withdraw_decs = State()
    Withdraw_decs_with_some_bots = State()
    Skip_quest = State()
    Send_cards = State()
    Send_cards_from_some_bots = State()
    Send_cards_choose_player = State()
