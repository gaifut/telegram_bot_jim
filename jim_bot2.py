import time
import logging
from aiogram import Bot, Dispatcher, executor, types
import asyncio


from constants import API_KEY

MSG1 = "Have you coded today {}?"

# Configure logging
logging.basicConfig(filename = 'test.log',level=logging.INFO)

# create bot and dispatcher
bot = Bot(API_KEY)
dp = Dispatcher(bot)

# handling incoming messages
@dp.message_handler(commands = ['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    await message.reply( f"Hey, {user_name}!")

    logging.info(f'{user_id} {user_full_name} {time.asctime()}')

    for i in range(7):
        time.sleep(60*1)
        await bot.send_message(user_id, MSG1.format(user_name))


if __name__ == '__main__':
    executor.start_polling(dp)