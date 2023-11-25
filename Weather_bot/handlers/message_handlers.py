from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon import LEXICON, LEXICON_COUNTRIES
from keyboards.builder_keyboards import create_inline_keyboard, keyboard
from config.config import Config, load_config
from services.services import get_weather
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

config: Config = load_config()
api_key = config.Weather_bot.api_key

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON['/help'])

@router.message(Command(commands='weather'))
async def process_weather_command(message: Message):
    await message.answer(LEXICON['/weather'], reply_markup=keyboard)

@router.message(F.text == LEXICON['/weather_geo'])
async def process_accept_geo(message: Message):
    pass

@router.message(F.text == LEXICON['/weather_chose'])
async def process_town_chose(message: Message):
    buttons = [KeyboardButton(text=city) for city in LEXICON_COUNTRIES]
    row_width = 2
    keyboard = ReplyKeyboardMarkup(keyboard=[buttons[i:i + row_width] for i in range(0, len(buttons), row_width)], resize_keyboard=True)

    await message.answer("Выберите город из списка:", reply_markup=keyboard)

@router.message()
async def send_echo(message: Message):
    await message.answer(f'Неизвестная команда. Ваше сообщение: {message.text}')