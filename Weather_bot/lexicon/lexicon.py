LEXICON: dict[str, str] = {
    '/start': '<b>Привет, пользователь!</b>\n\nЭто бот, в котором '
              'ты можешь получить информацию о погоде в реальном времени '
              'о 32 городах.\n\nДля справки /help',
    '/help': '<b>Это бот-погода</b>\n\nДоступные команды:\n\n',
    '/weather': '<b>Вы хотите использовать геолокацию или выбрать город вручную?</b>',
    '/weather_geo': 'Отправить геолокацию',
    '/weather_chose': 'Выбрать вручную'
}


LEXICON_COMMANDS: dict[str, str] = {
    '/help': 'Справка по работе бота',
    #...
}

LEXICON_COUNTRIES = [
    "New York,US", "London,GB", "Paris,FR", "Berlin,DE", "Moscow,RU", "Los Angeles,US",
    "Tokyo,JP", "Sydney,AU", "Beijing,CN", "Toronto,CA", "Rome,IT", "Madrid,ES", "Athens,GR",
    "Cairo,EG", "Dubai,AE", "Bangkok,TH", "Mumbai,IN", "Rio de Janeiro,BR", "Buenos Aires,AR",
    "Cape Town,ZA", "Stockholm,SE", "Oslo,NO", "Helsinki,FI", "Dublin,IE", "Amsterdam,NL",
    "Brussels,BE", "Vienna,AT", "Zurich,CH", "Warsaw,PL", "Prague,CZ", "Budapest,HU", "Lisbon,PT"
]