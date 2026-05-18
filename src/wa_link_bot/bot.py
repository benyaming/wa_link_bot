from __future__ import annotations

import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

from wa_link_bot.phone import extract_whatsapp_number, whatsapp_link


def _load_environment() -> None:
    load_dotenv(".env")


def _default_country_code() -> str:
    return os.getenv("DEFAULT_COUNTRY_CODE", "972")


async def start(message: Message) -> None:
    await message.answer("Send me a phone number and I will return a WhatsApp link.")


async def phone_to_whatsapp(message: Message) -> None:
    phone_number = extract_whatsapp_number(
        message.text or "",
        default_country_code=_default_country_code(),
    )
    if phone_number is None:
        await message.answer("Send a phone number, for example: 0544445811")
        return

    await message.answer(whatsapp_link(phone_number))


async def run() -> None:
    _load_environment()
    logging.basicConfig(level=logging.INFO)

    token = os.getenv("BOT_TOKEN") or os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise SystemExit("Set BOT_TOKEN before running the bot.")

    bot = Bot(token=token)
    dispatcher = Dispatcher()
    dispatcher.message.register(start, CommandStart())
    dispatcher.message.register(phone_to_whatsapp, F.text)

    await dispatcher.start_polling(bot)


def main() -> None:
    asyncio.run(run())


if __name__ == "__main__":
    main()
