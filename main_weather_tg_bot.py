# pip install requests
# pip install aiogram
import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
from aiogram.types.message import ContentType

bot = Bot(token=tg_bot_token) # Токен для телеграм бота
dp = Dispatcher(bot) # Просто сокращение)
cany="BAACAgIAAxkBAAIB3mOPcpGSMA4ZzPZugnpnpY5OazOpAAJCIwACLwmBSFt09M35Pd3iKwQ"
tim='AgACAgIAAxkBAAIDEmOQy6xWoaKZb7KqxaoGeEmJ6fy_AAJdwDEbsnKISI3jydK__ESwAQADAgADcwADKwQ'
karmagedon='BAACAgIAAxkBAAIDQmOQzjHx1kuc4MIgxRqg86TB-nDXAAJtJQACLwmJSA2E_PwYhsAAASsE'

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("КОМАНДЫ")
    await message.answer("/start - Начало")
    await message.answer("/cany - пасхалка с саньком")
    await message.answer("/potato - пасхалка с тимошкой")
    await message.answer("/karmagedon - пасхалка с кизару")

@dp.message_handler(commands=['cany'])
async def process_video2_command(message: types.Message):
    caption = 'Саня'
    await bot.send_video(message.from_user.id, cany,
                         reply_to_message_id=message.message_id)

@dp.message_handler(commands=['potato'])
async def process_photo_command(message: types.Message):
    caption = 'Пару мешков картошки'
    await bot.send_photo(message.from_user.id, tim,
                         reply_to_message_id=message.message_id)

@dp.message_handler(commands=['karmagedon'])
async def process_video_command1(message: types.Message):
    caption = 'Кармагедон у школьника'
    await bot.send_video(message.from_user.id, karmagedon,
                         reply_to_message_id=message.message_id)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Погода \U00002600")],
        [types.KeyboardButton(text="Отправить свой контакт ☎️", request_contact=True)],
        [types.KeyboardButton(text="Исходный код 👨‍💻")],
        [types.KeyboardButton(text="Секрет ❓")] # Подключаем клавиатуру из кнопок
    ]
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    await message.answer("Приветсвую тебя! Этот бот сейчас находится в разработке так, что не бомбите если не работает) \U0001F600", reply_markup=keyboard) # Приветствие

inline_btn_1 = types.InlineKeyboardButton('Весь код', callback_data='buttonGit', url='https://github.com/platon255/AbdulaBotPython') # Инлайн кнопка
inline_kb1 = types.InlineKeyboardMarkup().add(inline_btn_1)

# Пасхалки
@dp.message_handler(text='Секрет ❓')
async def process_command_1(message: types.Message):
    await message.answer(text="УУУ Секретики ❓❓❓")
    kb = [
    [types.KeyboardButton(text="Усач 👨")],
    [types.KeyboardButton(text="Картофель 🍟")],
    [types.KeyboardButton(text="Кармагедон 🌪")],
    [types.KeyboardButton(text="Меню 👥")] # Подключаем клавиатуру из кнопок
    ]
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    await message.answer("Выбирай секретик ...", reply_markup=keyboard) 

@dp.message_handler(text='Усач 👨')
async def process_video2_1_command(message: types.Message):
    await message.answer(text="Напиши в чат команду /help и узнаешь все секреты")

@dp.message_handler(text='Картофель 🍟')
async def process_photo_1_command(message: types.Message):
    await message.answer(text="Напиши в чат команду /help и узнаешь все секреты")

@dp.message_handler(text='Кармагедон 🌪')
async def process_video1_2_command(message: types.Message):
    await message.answer(text="Напиши в чат команду /help и узнаешь все секреты")

@dp.message_handler(text="Исходный код 👨‍💻")
async def process_command_2(message: types.Message):
    await message.answer(text="Ссылка на прокет на гит хабе \U0001F600", reply_markup=inline_kb1) # Функция которая выкидывает инлайн кнопку
    kb = [
    [types.KeyboardButton(text="Меню 👥")]  # Подключаем клавиатуру из кнопок
    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    await message.answer("Версия пока не вышла в открытый доступ ❌", reply_markup=keyboard) 

@dp.message_handler(text='Меню 👥')
async def cmd_start1(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Погода \U00002600")],
        [types.KeyboardButton(text="Отправить свой контакт ☎️", request_contact=True)],
        [types.KeyboardButton(text="Исходный код 👨‍💻")],
        [types.KeyboardButton(text="Секрет ❓")] # Подключаем клавиатуру из кнопок
    ]
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    await message.answer(text='Менюшечка', reply_markup=keyboard)

@dp.message_handler()
async def get_weather(message: types.Message):
    if message.text == 'Погода \U00002600':
        await message.reply("Привет! Ты просто можешь написать мне название города в любое время")
    else:
        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }

        try:
            r = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
            )
            data = r.json()

            city = data["name"]
            cur_weather = data["main"]["temp"]

            weather_description = data["weather"][0]["main"]
            if weather_description in code_to_smile:
                wd = code_to_smile[weather_description]
            else:
                wd = "Посмотри в окно, не пойму что там за погода!"

            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind = data["wind"]["speed"]
            sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
            length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
                data["sys"]["sunrise"])

            await message.reply(f"⚠️{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}⚠️\n"
                f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
                f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                f"Вот и вся погода ✅"
                )

        except:
            await message.reply("\U00002620 Проверьте название города \U00002620")

if __name__ == '__main__':
    executor.start_polling(dp)