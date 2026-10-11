import asyncio
import logging
from aiogram import Bot, Dispatcher
from keep_alive import keep_alive  # <--- ضفنا هذا السطر

from config import BOT_TOKEN
from handlers import router

logging.basicConfig(level=logging.INFO)

async def main():
    keep_alive()  # <--- ضفنا هذا السطر عشان يشتغل السيرفر الوهمي
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_router(router)
    print("🚀 البوت يعمل الآن...")
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
