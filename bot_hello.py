from aiogram import *

bot = Bot(token='6160771517:AAGublQICNRZ_Rlwo5LHr6UR5kD-RQOUQeo')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def hello(message):
    id_chat = message.from_user.id
    await bot.send_message(id_chat, 'Привет!!!')
    await bot.send_message(id_chat, 'Я бот-повторюшка ^.^')
    await bot.send_message(id_chat, 'Скажи мне что-нибудь')


if __name__ == '__main__':
    executor.start_polling(dp)






# {message.from_user.username}, я бот и я буду пытаться угадать, какое число ты загадал!
#    await bot.send_message(id_chat, 'Я бот-повторюшка ^.^')
#    await bot.send_message(id_chat, 'Скажи мне что-нибудь')