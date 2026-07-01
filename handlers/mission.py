from aiogram import Router
from aiogram.filters import Command

router = Router()

def get_mission():
    return {
        "workout": "50 отжиманий",
        "steps": "10000 шагов",
        "water": "2 литра воды",
        "reading": "30 минут чтения",
        "sleep": "до 23:00"
    }

@router.message(Command("mission"))
async def mission(message):
    m = get_mission()

    await message.answer(
        "⚔️ МИССИЯ ДНЯ\n\n"
        f"💪 {m['workout']}\n"
        f"🚶 {m['steps']}\n"
        f"💧 {m['water']}\n"
        f"📖 {m['reading']}\n"
        f"😴 {m['sleep']}"
    )
