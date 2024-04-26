from aiogram import Bot

from config import get_settings

bot: Bot | None = None

config = get_settings()
def get_bot() -> Bot:
    global bot

    if not bot:
        bot = Bot(token=config.telegram_token)  # Объект бота
    return bot
