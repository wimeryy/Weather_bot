from lexicon.lexicon import LEXICON
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def create_inline_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON[button] if button in LEXICON else button,
        callback_data=button) for button in buttons]
    )
    return kb_builder.as_markup()

kb_builder = ReplyKeyboardBuilder()

geo_btn = KeyboardButton(
    text=LEXICON['/weather_geo'],
    request_location=True
)

geo_chose = KeyboardButton(
    text=LEXICON['/weather_chose'],
)

kb_builder.row(geo_btn, geo_chose, width=1)
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)
