"""
سلف‌بات ساده تلگرام با Telethon
- تو هر گپی که (از اکانت اصلی) بنویسی «میو فعال» → هر ۱۰ دقیقه (پیش‌فرض) یک بار «میو» می‌فرسته
- می‌تونی زمان دلخواه رو هم بدی، مثلاً: «میو فعال 3» → هر ۳ دقیقه
- بنویس «میو غیرفعال» → توی همون گپ خاموش میشه
- ادمین(ها) می‌تونن از طریق پیوی به همین اکانت، آیدی عددی یک گپ رو بفرستن
  تا میو توی اون گپ فعال بشه (بدون نیاز به تایپ کردن تو خود گپ)
  برای زمان دلخواه: آیدی و بعد یه فاصله و عدد دقیقه، مثلاً: -1001234567890 5

نصب پیش‌نیاز:
    pip install telethon

قبل از اجرا:
    1) برو به https://my.telegram.org و یه اپلیکیشن بساز
    2) مقدار api_id و api_hash رو زیر جایگزین کن
    3) آیدی عددی ادمین(ها) رو توی ADMIN_IDS بذار (خودت می‌تونی آیدی عددی خودتم بذاری)
    4) اولین بار که اجرا می‌کنی، شماره تلفن و کد تایید رو ازت می‌پرسه
       و بعدش یه فایل session ساخته میشه که دیگه لازم نیست دوباره لاگین کنی

نکته امنیتی:
    هر آیدی که تو ADMIN_IDS بذاری، می‌تونه از راه دور باعث بشه اکانتت
    توی هر گپی که عضوشی (فقط با فرستادن آیدی عددیش) پیام خودکار بفرسته.
    فقط آیدی‌هایی که بهشون اعتماد کامل داری رو اضافه کن.
"""

import asyncio
from telethon import TelegramClient, events

# ====== تنظیمات ======
api_id = 35263817          # <-- اینجا رو با api_id خودت جایگزین کن
api_hash = "8f221cbae9e25cdafba56e897ed39b5e"  # <-- اینجا رو با api_hash خودت جایگزین کن
session_name = "setare"
default_interval_minutes = 10  # اگه زمان دستی داده نشه، این مقدار استفاده میشه

# آیدی عددی حساب‌هایی که اجازه دارن از طریق پیوی، گپ رو فعال کنن
ADMIN_IDS = [5888377320]  # <-- آیدی عددی خودت/ادمین رو اینجا جایگزین کن
# ======================

client = TelegramClient(session_name, api_id, api_hash)

# ذخیره‌ی تسک‌های فعال هر گپ: chat_id -> asyncio.Task
active_tasks: dict[int, asyncio.Task] = {}


async def meow_loop(chat_id: int, interval_minutes: float):
    """هر interval_minutes دقیقه یک بار «میو» می‌فرسته تا وقتی کنسل بشه"""
    interval_seconds = interval_minutes * 60
    try:
        while True:
            await asyncio.sleep(interval_seconds)
            try:
                await client.send_message(chat_id, "میو")
            except Exception as e:
                print(f"خطا در ارسال پیام به {chat_id}: {e}")
    except asyncio.CancelledError:
        pass


def activate_meow(chat_id: int, interval_minutes: float = default_interval_minutes) -> bool:
    """اگه از قبل فعال نبود، فعالش می‌کنه (با فاصله‌ی دلخواه) و True برمی‌گردونه"""
    if chat_id in active_tasks:
        return False
    active_tasks[chat_id] = asyncio.create_task(meow_loop(chat_id, interval_minutes))
    return True


def deactivate_meow(chat_id: int) -> bool:
    """اگه فعال بود، خاموشش می‌کنه و True برمی‌گردونه"""
    task = active_tasks.pop(chat_id, None)
    if task:
        task.cancel()
        return True
    return False


# --- فعال/غیرفعال کردن با نوشتن در خود گپ (از اکانت اصلی) ---
# نمونه: «میو فعال» (زمان پیش‌فرض) یا «میو فعال 3» (هر ۳ دقیقه)
@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    text = event.raw_text.strip()
    chat_id = event.chat_id
    parts = text.split()

    if parts and parts[0] == "میو" and len(parts) >= 2 and parts[1] == "فعال":
        interval_minutes = default_interval_minutes
        if len(parts) >= 3:
            try:
                interval_minutes = float(parts[2])
                if interval_minutes <= 0:
                    raise ValueError
            except ValueError:
                await event.reply("عدد دقیقه نامعتبره. مثال درست: میو فعال 5")
                return

        if activate_meow(chat_id, interval_minutes):
            await event.reply(f"میو فعال شد ✅ (هر {interval_minutes:g} دقیقه)")
        else:
            await event.reply("میو از قبل فعال بود 🐱")

    elif text == "میو غیرفعال":
        if deactivate_meow(chat_id):
            await event.reply("میو غیرفعال شد ❌")
        else:
            await event.reply("میو تو این گپ فعال نبود")


# --- فعال کردن از راه دور: ادمین از پیوی، آیدی عددی گپ رو می‌فرسته ---
# نمونه: «-1001234567890» (زمان پیش‌فرض) یا «-1001234567890 5» (هر ۵ دقیقه)
@client.on(events.NewMessage(incoming=True))
async def admin_handler(event):
    if not event.is_private:
        return

    sender_id = event.sender_id
    if sender_id not in ADMIN_IDS:
        return

    text = event.raw_text.strip()
    parts = text.split()
    if not parts:
        return

    # بخش اول باید آیدی عددی گپ باشه (برای گروه/سوپرگروه ممکنه با - شروع بشه)
    if not parts[0].lstrip("-").isdigit():
        return

    target_chat_id = int(parts[0])
    interval_minutes = default_interval_minutes

    if len(parts) >= 2:
        try:
            interval_minutes = float(parts[1])
            if interval_minutes <= 0:
                raise ValueError
        except ValueError:
            await event.reply("عدد دقیقه نامعتبره. مثال درست: -1001234567890 5")
            return

    if activate_meow(target_chat_id, interval_minutes):
        await event.reply(f"میو برای گپ {target_chat_id} فعال شد ✅ (هر {interval_minutes:g} دقیقه)")
    else:
        await event.reply(f"میو از قبل تو گپ {target_chat_id} فعال بود 🐱")


async def main():
    await client.start()
    print("سلف‌بات اجرا شد. برای فعال‌سازی، تو هر گپی بنویس: میو فعال")
    print("یا از پیوی، آیدی عددی گپ مورد نظر رو بفرست.")
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
