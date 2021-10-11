from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
strategy_buttons = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton(text="Standart", callback_data="standart")],
        [InlineKeyboardButton(text="Quests", callback_data="only_quests")],
        [InlineKeyboardButton(text="Wins", callback_data="only_wins")],
 ])

check_buttons = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton(text="Check all bots", callback_data="check_all")],
        [InlineKeyboardButton(text="Check some bots", callback_data="check_some_bots")],
        [InlineKeyboardButton(text="Send a log file", callback_data="send_log_file")],
 ])

withdraw_buttons = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton(text="Withdraw from all bots", callback_data="withdraw_all_decs")],
        [InlineKeyboardButton(text="Withdraw from some bots", callback_data="withdraw_some_decs")],

 ])


send_cards_buttons = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton(text="Send from all bots", callback_data="send_all_cards")],
        [InlineKeyboardButton(text="Send from some bots", callback_data="send_some_cards")],

 ])

withdraw_player_wallet_buttons = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton(text="Withdraw to a player", callback_data="withdraw_to_player")],
        [InlineKeyboardButton(text="Withdraw on a wallet", callback_data="withdraw_on_wallet")],

 ])

menu_buttons_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Stop")
        ],
        [
            KeyboardButton(text="Check")
        ],
        [
            KeyboardButton(text="Set a strategy")
        ],
        [
            KeyboardButton(text="Withdraw decs")
        ],
        [
            KeyboardButton(text="Send cards")
        ],
        [
            KeyboardButton(text="Skip quests")
        ],

    ],
    resize_keyboard=True
)

menu_buttons_stop = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Start")
        ],
        [
            KeyboardButton(text="Check")
        ],
        [
            KeyboardButton(text="Set a strategy")
        ],
        [
            KeyboardButton(text="Withdraw decs")
        ],
        [
            KeyboardButton(text="Send cards")
        ],
        [
            KeyboardButton(text="Skip quests")
        ],

    ],
    resize_keyboard=True
)