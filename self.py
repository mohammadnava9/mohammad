"""
سلف‌بات ساده تلگرام با Telethon
- تو هر گپی که بنویسی «میو فعال» → هر ۱۰ دقیقه یک بار «میو» می‌فرسته
- بنویس «میو غیرفعال» → توی همون گپ خاموش میشه

نصب پیش‌نیاز:
    pip install telethon

قبل از اجرا:
    1) برو به https://my.telegram.org و یه اپلیکیشن بساز
    2) مقدار api_id و api_hash رو زیر جایگزین کن
    3) اولین بار که اجرا می‌کنی، شماره تلفن و کد تایید رو ازت می‌پرسه
       و بعدش یه فایل session ساخته میشه که دیگه لازم نیست دوباره لاگین کنی
"""

import asyncio
from telethon import TelegramClient, events

# ====== تنظیمات ======
api_id = 37414017          # <-- اینجا رو با api_id خودت جایگزین کن
api_hash = "e8befe4dd13055ea9dfa50b0cef5aa29"  # <-- اینجا رو با api_hash خودت جایگزین کن
session_name = "meow_session"
interval_seconds = 10 * 60  # هر ۱۰ دقیقه
# ======================

client = TelegramClient(session_name, api_id, api_hash)

# ذخیره‌ی تسک‌های فعال هر گپ: chat_id -> asyncio.Task
active_tasks: dict[int, asyncio.Task] = {}


async def meow_loop(chat_id: int):
    """هر interval_seconds ثانیه یک بار «میو» می‌فرسته تا وقتی کنسل بشه"""
    try:
        while True:
            await asyncio.sleep(interval_seconds)
            await client.send_message(chat_id, "میو")
    except asyncio.CancelledError:
        pass


@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    text = event.raw_text.strip()
    chat_id = event.chat_id

    if text == "میو فعال":
        if chat_id in active_tasks:
            await event.reply("میو از قبل فعال بود 🐱")
            return
        active_tasks[chat_id] = asyncio.create_task(meow_loop(chat_id))
        await event.reply("میو فعال شد ✅ (هر ۱۰ دقیقه)")

    elif text == "میو غیرفعال":
        task = active_tasks.pop(chat_id, None)
        if task:
            task.cancel()
            await event.reply("میو غیرفعال شد ❌")
        else:
            await event.reply("میو تو این گپ فعال نبود")


async def main():
    await client.start()
    print("سلف‌بات اجرا شد. برای فعال‌سازی، تو هر گپی بنویس: میو فعال")
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
