import subprocess
from pathlib import Path
from aiogram.types import  File
from get_bot import get_bot
from ffmpeg import Ffmpeg

bot = get_bot()

async def handle_file(file: File, file_name: str, path: str):
    """Функция сохраняет файл по указанному пути"""
    file_path_out = f'{path}\{file_name}'
    Path(f"{path}").mkdir(parents=True, exist_ok=True)

    await bot.download_file(file_path=file.file_path, destination=file_path_out)

async def convert_voice(file_name: str, path: str) -> File:
    """Функция конвертирует голосовое сообщение в формат wav с частотой дискретизации 16kHz"""
    try:
        file_path_in = f'{path}\{file_name}'
        file_path_out = f'{path}\convert_{file_name}.wav'
        FFMPEG_PATH = Ffmpeg().ffmpeg_path

        # Формируем команду для конвертирования аудио в WAV с декодированием в PCM
        command = [FFMPEG_PATH, "-i", file_path_in, "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "2",
                   file_path_out]

        # Выполняем команду с помощью subprocess
        subprocess.run(command, check=True)
        return file_path_out
    except subprocess.CalledProcessError as e:
        return ("Ошибка при конвертировании аудио:", e)
