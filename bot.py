import logging
import os
import shutil

from aiogram import Dispatcher, types
from aiogram.utils import executor
from open_cv import face_recognition
from config import get_settings
from get_bot import get_bot
from helpers import handle_file, convert_voice


bot = get_bot()
config = get_settings()
dp = Dispatcher(bot)  # Диспетчер для бота

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    filename="bot.log",
)


# Хэндлер на команду /start , /help
@dp.message_handler(commands=["start", "help"])
async def cmd_start(message: types.Message):
    await message.reply(
        "Привет! Я готов к работе."
    )


# Хэндлер на команду /test
@dp.message_handler(commands="test")
async def cmd_test(message: types.Message):
    """
    Обработчик команды /test
    """
    await message.answer("Test")


# Хэндлер на получение голосового сообщения
@dp.message_handler(content_types=[
    types.ContentType.VOICE
    ]
)
async def voice_message_handler(message: types.Message):
    """
    Обработчик на получение голосового и аудио сообщения.
    """

    path = config.voice_message_path
    file_id = message.voice.file_id

    # Скачивание файла
    file = await bot.get_file(file_id)
    file_name = f"{message.from_user.id}_{file.file_id}"
    await handle_file(file=file, file_name=file_name, path=path)
    await message.answer("Сообщение сохранено.")

    # Конвертация в нужный формат
    path_answer = await convert_voice(file_name=file_name, path=path)
    os.remove(f'{path}\{file_name}')

    await message.answer('Собщение обработано')
    await message.answer_document(open(path_answer, "rb"))


# Хэндлер на получение документа или изображения
@dp.message_handler(content_types=[
    types.ContentType.PHOTO
    ]
)
async def image_message_handler(message: types.Message):
    """
    Обработчик распознования лиц на изображении.
    """

    path = config.image_message_path
    temp_path = config.temp_image_message_path

    file_id = message.photo[0]['file_id']

    # Скачивание файла
    file = await bot.get_file(file_id)
    file_name = f"{message.from_user.id}_{file.file_id}.jpg"
    await handle_file(file=file, file_name=file_name, path=temp_path)

    # Распознование лиц
    result = await face_recognition(file_name=file_name, path=temp_path)

    if not result:
        await message.answer("Лиц на изображении не обнаружено.")
        os.remove(f'{temp_path}\{file_name}')
        return

    await message.answer(f"Лиц на изображении: {result}. Изображение сохранено.")
    shutil.move(f'{temp_path}\{file_name}', f'{path}\{file_name}')



if __name__ == "__main__":
    # Запуск бота
    print("Запуск бота")
    try:
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        pass
