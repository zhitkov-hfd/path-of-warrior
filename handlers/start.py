from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "⚔️ PATH OF WARRIOR\n\n"
        "Добро пожаловать, воин.\n\n"
        "🎯 /mission — Миссия дня\n"
        "🔥 /report — Отчёт"
    )
