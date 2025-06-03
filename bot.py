
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN
from utils.pdf_generator import generate_pdf

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("👋 Вітаю! Я ваш юридичний помічник. Надішліть текст для PDF.")

@dp.message_handler()
async def generate_doc(message: types.Message):
    file_path = generate_pdf(message.text, message.from_user.id)
    with open(file_path, 'rb') as doc:
        await message.answer_document(doc, caption="Ваш документ готовий!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
