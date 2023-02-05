import time
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)


TOKEN = '5760224801:AAEbqZN4SUmO99F8YVTSzFItTCGnas34gXU'
MSG1 = "Have you coded today {}?"

bot = Bot(token = TOKEN)
dp = Dispatcher(bot = bot)

@dp.message_handler(commands = ['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.INFO(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Hey, {user_name}!")

    for i in range(10):
        time.sleep(2)
        await bot.send_message(user_id, MSG1.format(user_name))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)