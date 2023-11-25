LEXICON: dict[str, str] = {
    '/start': '🌦️ <b>Привет, пользователь!</b> 🌈'
              '\n\nЭто умный бот, где ты можешь моментально узнать актуальную информацию о погоде в 32 городах. ☀️🌧️❄️'
              '\n\nДля получения справки, просто напиши /help'
              '\nИли сразу начинай использование /weather 🤖✨'
              '\n\nВсе данные предоставлены weatherstack.com',
    '/help': '🌦️ <b>Это бот-погода</b> 🌈'
             '\n\nДоступные команды:'
             '\n\n🌅 /weather - Начать использовать бота',
    '/weather': '<b>Вы хотите использовать геолокацию или выбрать город вручную?</b>',
    '/weather_geo': 'Отправить геолокацию 📍',
    '/weather_chose': 'Выбрать вручную 👌',
    '/weather_text': '🌦 Нажимайте на название города и получайте информацию о погоде в реальном времени!'
                    '\n\n✨ Солнечное приключение начинается с вас! Выберите город, и мы предоставим вам самые актуальные данные о погоде.'
                    'Погружайтесь в мир прогнозов, оформленный в ярких тонах, чтобы ваш день был таким же ярким, как и информация, которую вы узнаете.'
}


LEXICON_COMMANDS: dict[str, str] = {
    '/help': 'Справка по работе бота',
    '/weather': 'Получить информацию о погоде'
}


LEXICON_COUNTRIES = [
    "New York,US", "London,GB", "Paris,FR", "Berlin,DE", "Moscow,RU", "Los Angeles,US",
    "Tokyo,JP", "Sydney,AU", "Beijing,CN", "Toronto,CA", "Rome,IT", "Madrid,ES", "Athens,GR",
    "Cairo,EG", "Dubai,AE", "Bangkok,TH", "Mumbai,IN", "Rio de Janeiro,BR", "Buenos Aires,AR",
    "Cape Town,ZA", "Stockholm,SE", "Oslo,NO", "Helsinki,FI", "Dublin,IE", "Amsterdam,NL",
    "Brussels,BE", "Vienna,AT", "Zurich,CH", "Warsaw,PL", "Prague,CZ", "Budapest,HU", "Lisbon,PT",
    "Taldykorgan,KZ", "Sevastopol,RU"
]

LEXICON_EMODJI: dict[str, str] = {
    'Clear': '☀️',
    'Overcast': '☁️',
    'Sunny': '☀️',
    'Patchy light drizzle': '🌧️',
    'Partly cloudy': '🌤️',
    'Light Snow': '❄️',
    'Patchy rain possible': '🌦️',
    'Freezing fog': '🌫️❄️',
    'Hail': '🌨️',
    'Windy': '💨',
    'Foggy': '🌫️',
    'Snowy': '❄️',
    'Thunderstorms': '⛈️',
    'Showers': '🌦️',
    'Rainy': '🌧️',
    'Cloudy': '☁️',
    'Heavy snow': '❄️❄️'
}