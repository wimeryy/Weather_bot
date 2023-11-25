from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon import LEXICON, LEXICON_COUNTRIES
from keyboards.builder_keyboards import create_inline_keyboard, keyboard
from services.services import get_weather_city, get_weather_geo
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


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

@router.message(F.text == None)
async def process_get_weather_geo(message: Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    weather_data = get_weather_geo(latitude, longitude)
    if weather_data is not None:
        await message.answer(weather_data)
    else:
        await message.answer("Не удалось получить данные о погоде.")

@router.message(F.text == LEXICON['/weather_chose'])
async def process_city_chose(message: Message):
    buttons = [KeyboardButton(text=city) for city in LEXICON_COUNTRIES]
    row_width = 2
    keyboard = ReplyKeyboardMarkup(keyboard=[buttons[i:i + row_width] for i in range(0, len(buttons), row_width)], resize_keyboard=True)

    await message.answer(LEXICON['/weather_text'], reply_markup=keyboard)

@router.message(F.text.in_(LEXICON_COUNTRIES))
async def process_get_weather(message: Message):
    city = message.text
    await message.answer(get_weather_city(city=city))

@router.message()
async def send_echo(message: Message):
    await message.answer(f'Неизвестная команда. Ваше сообщение: {message.text}')