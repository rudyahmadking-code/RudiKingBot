import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
AI_API_KEY = os.getenv("AI_API_KEY")  # <--- هذا السطر كان ناقص

if not BOT_TOKEN:
    raise ValueError("⚠️ التوكن غير موجود في ملف .env")
if not AI_API_KEY:
    raise ValueError("⚠️ مفتاح الذكاء الاصطناعي غير موجود في ملف .env")
