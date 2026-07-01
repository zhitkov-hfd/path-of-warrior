from aiogram import Router
from aiogram.filters import Command

router = Router()

@router.message(Command("report"))
async def report(message):
    await message.answer(
        "🔥 Отчёт принят.\n"
        "Завтра ты станешь сильнее."
    )
