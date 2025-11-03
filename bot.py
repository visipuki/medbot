import os
import logging
from aiogram import Bot, Dispatcher, executor, types

# Получение токена бота из переменных окружения
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Проверка наличия токена
if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN не установлен в окружении!")

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаём объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Пример простой команды /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я помогу тебе не забыть про лекарства.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
