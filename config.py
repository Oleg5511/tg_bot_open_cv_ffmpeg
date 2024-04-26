import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), ".env")

class Settings(BaseSettings):
    # Название проекта.
    project_name: str = Field(
        "Тестовое задания для ID R&D",
        description="Название проекта",
    )
    project_description: str = Field(
        "Бот умеет конвертировать голосовые в .wav формат и распозновать лица на фотографиях",
        description="Описание проекта",
    )
    project_version: str = Field("0.0.1", description="Версия проекта")

    telegram_token: str = Field(description="Токен бота телеграмма")

    # Пути сохранения файлов
    voice_message_path: str = Field(r"C:\Users\ogurskiy\Music", description="Путь сохранения аудио сообщения")
    image_message_path: str = Field(r"C:\Users\ogurskiy\Pictures",
                                    description="Путь сохранения фотографии, на которой были распознаны лица")
    temp_image_message_path: str = Field(r"C:\Users\ogurskiy\Pictures\temp",
                                         description="Временное хранилище изображений для распознования лиц")
    model_config = SettingsConfigDict(env_file=DOTENV)



conf: Settings | None = None


def get_settings() -> Settings:
    global conf

    if not conf:
        conf = Settings()
    return conf