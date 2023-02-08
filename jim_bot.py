import time
import logging

from aiogram import Bot, Dispatcher, executor, types
from constants import API_KEY

logging.basicConfig(level=logging.INFO)


MSG1 = "Have you coded today {}?"

bot = Bot(token = API_KEY)
dp = Dispatcher(bot = bot)

@dp.message_handler(commands = ['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    await message.reply(f"Hey, {user_name}!")

    for i in range(7):
        time.sleep(60*1)
        await bot.send_message(user_id, MSG1.format(user_name))

    #logging.INFO(f'{user_id=} {user_full_name=} {time.asctime()}')

if __name__ == '__main__':
    executor.start_polling(dp)