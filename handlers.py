from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from openai import AsyncOpenAI
from config import AI_API_KEY

router = Router()

# تهيئة عميل Groq (يستخدم نفس صيغة OpenAI)
client = AsyncOpenAI(
    api_key=AI_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("أهلاً بك! أنا بوت ذكي مجاني 100%، اسألني أي شي. 🧠⚡")

@router.message()
async def ai_handler(message: Message):
    try:
        # إظهار حالة "يكتب..." في تيليجرام
        await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
        
        # إرسال رسالة المستخدم إلى Groq
        response = await client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": "أنت مساعد ذكي وودود. تجيب باللغة العربية بأسلوب مختصر ومفيد."},
                {"role": "user", "content": message.text}
            ]
        )
        
        # استلام الرد وإرساله للمستخدم
        ai_reply = response.choices[0].message.content
        await message.answer(ai_reply)
        
    except Exception as e:
        # طباعة الخطأ الحقيقي في الـ Terminal
        print(f"❌ خطأ في الذكاء الاصطناعي: {e}")
        await message.answer("عذراً، حدث خطأ أثناء معالجة طلبك. حاول مرة أخرى.")
