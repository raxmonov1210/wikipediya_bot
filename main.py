import logging
import wikipedia

wikipedia.set_lang('uz')



from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5856105139:AAFuvcVnAhiK1fxKMhmICGMHSXq2VBIXDUE'

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
    # try:
    #     respond = wikipedia.summary(message.text)
    #     await message.answer(respond)
    # except:
    #     await message.answer("Bu mavzuga oid maqola topilmadi")

    try:
        res = wikipedia.summary(message.text)
        await message.answer(res)
    except:
        await message.answer("Hech narsa topilmadi")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)