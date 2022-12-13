import logging
import wikipedia

wikipedia.set_lang('uz')



from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'Bot_token'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    
    await message.reply("Salom bot hush kelibsiz")



@dp.message_handler()
async def echo(message: types.Message):
    try:
        res = wikipedia.summary(message.text)
        await message.answer(res)
    except:
        await message.answer("Hech narsa topilmadi")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
