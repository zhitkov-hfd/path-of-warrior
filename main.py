import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers import start, mission, report

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(start.router)
    dp.include_router(mission.router)
    dp.include_router(report.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
