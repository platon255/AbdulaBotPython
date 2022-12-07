
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

# Получаем айди видео
@dp.message_handler(content_types=["video"]) 
async def video_file_id(message: types.Message):
    await bot.send_message(message.from_user.id, "Ваше id video")
    await message.answer(message.video.file_id)
# id photo
@dp.message_handler(content_types=['photo'])
async def scan_message(msg: types.Message):
    document_id = msg.photo[0].file_id
    file_info = await bot.get_file(document_id)
    print(f'file_id: {file_info.file_id}')
    print(f'file_path: {file_info.file_path}')
    print(f'file_size: {file_info.file_size}')
    print(f'file_unique_id: {file_info.file_unique_id}')

if __name__ == '__main__':
    executor.start_polling(dp)