from aiogram import *
import time

bot = Bot(token='6160771517:AAGublQICNRZ_Rlwo5LHr6UR5kD-RQOUQeo')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def hello(message:types.message):
    global middle, lower_bound, upper_bound, count
    global keyboard
    lower_bound = 1
    upper_bound = 100   
    count = 1
    middle = (lower_bound + upper_bound) // 2
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}, я бот и я буду пытаться угадать, какое число ты загадал!')
    await bot.send_message(message.from_user.id, 'Придумай число от 1 до 100')
    time.sleep(2)
    await bot.send_message(message.from_user.id,'3')
    time.sleep(0.5)
    await bot.send_message(message.from_user.id,'2')
    time.sleep(0.5)
    await bot.send_message(message.from_user.id,'1')
    time.sleep(0.5)
    await bot.send_message(message.from_user.id,'Поехали!')
    time.sleep(0.5)
    keys = [types.InlineKeyboardButton('Моё число больше', callback_data='more'), 
            types.InlineKeyboardButton('Моё число меньше', callback_data='less'), 
            types.InlineKeyboardButton('Ты угадал!', callback_data='guess')]
    keyboard = types.InlineKeyboardMarkup(row_width=1).add(*keys)
    await bot.send_message(message.from_user.id, f'Это число {middle}?', reply_markup=keyboard)


@dp.callback_query_handler(text='more')
async def more(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    global lower_bound, middle, keyboard, count
    count += 1
    lower_bound = middle + 1
    middle = (lower_bound + upper_bound) // 2
    await bot.send_message(call.from_user.id, ':((')
    await bot.send_message(call.from_user.id, f'Это число {middle}?', reply_markup=keyboard)


@dp.callback_query_handler(text='less')
async def less(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    global upper_bound, middle, keyboard, count
    count += 1
    upper_bound = middle - 1
    middle = (lower_bound + upper_bound) // 2
    await bot.send_message(call.from_user.id, ':((')
    await bot.send_message(call.from_user.id, f'Это число {middle}?', reply_markup=keyboard)


@dp.callback_query_handler(text='guess')
async def end(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await bot.send_sticker(call.from_user.id, sticker='CAACAgIAAxkBAAEJL3RkeapGmPnyZivWQAvZMpYQSljoNAACPEIAAulVBRjY85LIi7Sm5S8E')
    await bot.send_message(call.from_user.id, 'Если хотите начать сначала, нажмите на /start')


    
if __name__ == '__main__':
    executor.start_polling(dp)



