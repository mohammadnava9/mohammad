"""
سلف‌بات تلگرام با Telethon
ساخته شده توسط @MRZverse

قابلیت‌ها:
  - «میو فعال» / «میو غیرفعال»           → پیام دوره‌ای «میو» توی همون گپ
  - «.فونت <متن>»                        → تبدیل متن به چند سبک یونیکد (بولد، ایتالیک، دست‌نویس و...)
  - «اسم فونت <سبک> <متن>»               → گذاشتن اسم پروفایل با یه سبک فونت خاص (مثال: اسم فونت Sans Mohammad)
  - «ساعت بیو فعال» / «ساعت بیو غیرفعال»  → آپدیت خودکار بیو با ساعت لحظه‌ای
  - «ساعت اسم فعال» / «ساعت اسم غیرفعال» → آپدیت خودکار نام خانوادگی با ساعت لحظه‌ای
  - «.پینگ»                              → سرعت پاسخ‌دهی اکانت (ms)
  - «افک فعال <پیام دلخواه>» / «افک غیرفعال» → جواب خودکار به اولین پیام خصوصی هر نفر وقتی نیستی
  - «.آیدی»                              → آیدی همین گپ، یا اگه ریپلای بزنی آیدی همون کاربر
  - «.اطلاعات» (روی ریپلای)              → نام، یوزرنیم، آیدی و بیوی کاربر
  - «.پاک <عدد>»                         → پاک کردن N تا از پیام‌های اخیر خودت توی همون گپ
  - «.حساب <عبارت>»                      → ماشین‌حساب (مثال: .حساب (5+3)*2)
  - «.حذف <ثانیه> <متن>»                 → ارسال پیام که بعد از N ثانیه خودش پاک میشه
  - «.تایپ <متن>»                        → قبل از ارسال پیام، چند ثانیه «در حال تایپ...» نشون میده
  - «ربات روشن» / «ربات خاموش»           → سوییچ کلی، وقتی خاموشه فقط همین دستور کار می‌کنه
  - «.آمار»                              → تعداد گروه‌ها، کانال‌ها و چت‌های خصوصی
  - «خوانده‌شدن پیوی فعال/غیرفعال» / «خوانده‌شدن گروه فعال/غیرفعال» → خوانده‌شدن خودکار، جدا برای پیوی و گروه
  - «.نشست‌ها»                           → لیست دستگاه‌های لاگین‌شده روی اکانت
  - «.ذخیره» (روی ریپلای)                → پیام رو توی سیو مسیجز ذخیره می‌کنه
  - «.بلاک» / «.آنبلاک» (روی ریپلای)     → بلاک/آنبلاک کردن کاربر
  - «.کوتاه <لینک>»                      → کوتاه‌کردن لینک با TinyURL
  - «.ساعت <منطقه>»                      → ساعت محلی (ایران، لندن، دبی، نیویورک، توکیو)
  - «.ترجمه <متن>»                       → ترجمه خودکار فارسی↔انگلیسی
  - «.پاسخ‌سریع تنظیم <کلمه> | <جواب>»    → افزودن پاسخ خودکار برای یه کلمه
  - «.پاسخ‌سریع حذف <کلمه>» / «.پاسخ‌سریع پاک» / «.پاسخ‌سریع لیست»
  - «.راهنما»                            → آموزش کامل همه‌ی دستورها
  - «فارم میویی فعال» / «فارم میویی غیرفعال» → فرستادن خودکار «پیشی» به بات Meowie و کلیک روی دکمه‌ی برداشت، هر ۱ ساعت

قابلیت‌های تازه‌ی مدیریتی:
  - ساعت خودکار بیو/اسم حالا با فونت دابل-استرایک شیک نمایش داده میشه
  - مدیر توی پیوی می‌تونه بنویسه «میو فعال 5» تا فاصله‌ی دلخواه (به دقیقه) رو تنظیم کنه
  - مدیر می‌تونه بنویسه «mio online is gp» تا ازش آیدی عددی یا لینک یه گروه دیگه
    خواسته بشه؛ بعد از فرستادنش، میو توی همون گروه (با فاصله‌ی دلخواه در صورت نیاز) فعال میشه

قابلیت مدیریتی (کنترل با یک اکانت دوم):
  - آیدی عددی اکانت‌های مدیر رو توی ADMIN_IDS بذار.
  - مدیر می‌تونه توی پیوی خودِ همین اکانت (نه هرجای دیگه) دستورهای زیر رو بفرسته:
      میو فعال / میو غیرفعال، افک فعال / افک غیرفعال، ساعت بیو فعال/غیرفعال، ساعت اسم فعال/غیرفعال
  - مدیر می‌تونه توی هر گپی (گروه یا پیوی) روی هر پیامی که خودِ اکانت فرستاده ریپلای بزنه
    و کلمه‌ی «پاک» رو بنویسه تا همون پیام حذف بشه.

نصب پیش‌نیاز:
    pip install telethon

قبل از اجرا:
    1) برو به https://my.telegram.org و یه اپلیکیشن بساز
    2) مقدار api_id و api_hash رو زیر جایگزین کن
    3) اولین بار که اجرا می‌کنی، شماره تلفن و کد تایید رو ازت می‌پرسه
       و بعدش یه فایل session ساخته میشه که دیگه لازم نیست دوباره لاگین کنی

⚠️ نکته مهم درباره ساعت خودکار بیو/اسم:
    تلگرام محدودیت نرخ (flood limit) برای آپدیت پروفایل داره. اگه فاصله رو خیلی
    کم بذاری (مثلاً چند ثانیه)، ممکنه اکانتت موقتاً محدود بشه. فاصله‌ی پیش‌فرض
    (۶۰ ثانیه) امن‌تره؛ اگه خواستی تندترش کنی، خودت مسئولیت ریسکش رو بپذیر.
"""

import asyncio
import ast
import operator
import urllib.request
import urllib.parse
import json
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest, GetAuthorizationsRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest

# ====== تنظیمات ======
api_id = 30213358          # <-- اینجا رو با api_id خودت جایگزین کن
api_hash = "74b35d20203b6670dafcc595f81c4e46"  # <-- اینجا رو با api_hash خودت جایگزین کن
session_name = "meow_session4"
interval_seconds = 10 * 60      # فاصله‌ی پیام میو (۱۰ دقیقه)
clock_interval_seconds = 60     # فاصله‌ی آپدیت ساعت بیو/اسم (۶۰ ثانیه، توصیه‌شده)
tz_offset_hours = 3.5            # تایم‌زون تهران (UTC+3:30) - در صورت نیاز عوض کن
ADMIN_IDS: list[int] = [5888377320]        # <-- آیدی عددی اکانت‌های مدیر (برای گرفتنش: به @userinfobot پیام بده)
MEOWIE_BOT_USERNAME = "@MeowieQBot"  # <-- یوزرنیم واقعی بات میویی رو اینجا بذار
MEOWIE_TRIGGER_TEXT = "پیشی"          # کلمه‌ای که باید بهش فرستاده بشه
MEOWIE_BUTTON_KEYWORD = "برداشت میو پوینت ها"      # بخشی از متن دکمه‌ی «برداشت میو پوینت‌ها» که باید کلیک بشه
MEOWIE_FARM_INTERVAL_SECONDS = 60 * 60  # هر یک ساعت
# ======================

client = TelegramClient(session_name, api_id, api_hash)

# تسک‌های فعال میو: chat_id -> asyncio.Task
active_tasks: dict[int, asyncio.Task] = {}

# تسک‌های ساعت خودکار (فقط یک‌دونه از هرکدوم می‌تونه فعال باشه، چون پروفایل یکیه)
clock_bio_task: asyncio.Task | None = None
clock_name_task: asyncio.Task | None = None

# تسک فارم خودکار بات میویی
farm_task: asyncio.Task | None = None

# حالت افک (دور از دسترس)
afk_enabled = False
afk_message = "فعلاً نیستم، بعداً جواب می‌دم 🌙"
afk_replied_chats: set[int] = set()  # جلوگیری از ریپلای تکراری به یک گپ

# سوییچ کلی روشن/خاموش (وقتی خاموشه، فقط دستور روشن کردن پردازش میشه)
bot_enabled = True

# حالت خوانده‌شدن خودکار پیام‌ها (جدا برای پیوی و گروه)
markread_private_enabled = False
markread_group_enabled = False

# پاسخ‌های سریع: کلمه‌کلیدی -> جواب
quick_replies: dict[str, str] = {}

# منطقه‌های زمانی رایج برای دستور «.ساعت»
TIMEZONES = {
    "ایران": "Asia/Tehran", "iran": "Asia/Tehran", "tehran": "Asia/Tehran",
    "لندن": "Europe/London", "london": "Europe/London",
    "دبی": "Asia/Dubai", "dubai": "Asia/Dubai",
    "نیویورک": "America/New_York", "newyork": "America/New_York",
    "توکیو": "Asia/Tokyo", "tokyo": "Asia/Tokyo",
}

# آیدی مدیرهایی که الان منتظرن آیدی/لینک گروه رو برای فعال‌سازی میو بفرستن
admin_awaiting_group: set[int] = set()

HELP_TEXT = """📖 راهنمای سلف‌بات

🐱 میو
میو فعال [دقیقه] — فعال‌سازی میو (پیش‌فرض ۱۰ دقیقه)
میو غیرفعال

🕐 ساعت خودکار
ساعت بیو فعال/غیرفعال
ساعت اسم فعال/غیرفعال

🔤 فونت
.فونت <متن>
اسم فونت <سبک> <متن> (مثال: اسم فونت Sans Mohammad)

🌙 افک
افک فعال <پیام> / افک غیرفعال

👤 اطلاعات و مدیریت
.آیدی | .اطلاعات (روی ریپلای) | .پاک <عدد> | .بلاک/.آنبلاک (روی ریپلای)

🧮 ابزار
.حساب <عبارت> | .حذف <ثانیه> <متن> | .تایپ <متن> | .کوتاه <لینک> | .ساعت <منطقه> | .ترجمه <متن>

⚙️ سیستم
ربات روشن/خاموش | .آمار | .نشست‌ها | .ذخیره (روی ریپلای)
خوانده‌شدن پیوی/گروه فعال یا غیرفعال

💬 پاسخ سریع
.پاسخ‌سریع تنظیم <کلمه> | <جواب>
.پاسخ‌سریع حذف <کلمه> | .پاسخ‌سریع پاک | .پاسخ‌سریع لیست

🐱 فارم خودکار میویی
فارم میویی فعال / فارم میویی غیرفعال
(هر ساعت خودش «پیشی» رو به بات Meowie می‌فرسته و دکمه‌ی برداشت رو می‌زنه)

📡 دستورهای مخصوص مدیر (فقط توی پیوی همین اکانت)
میو فعال [دقیقه]، افک فعال/غیرفعال، ساعت بیو/اسم فعال/غیرفعال
mio online is gp → فعال‌سازی میو توی یه گروه دیگه با فرستادن آیدی عددی یا لینک اون گروه
روی هر پیام خودِ اکانت ریپلای بزن و بنویس «پاک» تا حذفش کنه

━━━━━━━━━━━━━━
ساخته شده توسط @MRZverse
"""


def now_str() -> str:
    tz = timezone(timedelta(hours=tz_offset_hours))
    return datetime.now(tz).strftime("%H:%M")


# ---------- توابع فعال/غیرفعال‌سازی مشترک (هم برای خودت، هم برای مدیر) ----------
async def toggle_meow(chat_id: int, minutes: float | None = None) -> str:
    if chat_id in active_tasks:
        return "میو از قبل فعال بود 🐱"
    seconds = (minutes * 60) if minutes else interval_seconds
    active_tasks[chat_id] = asyncio.create_task(meow_loop(chat_id, seconds))
    shown = minutes if minutes else interval_seconds / 60
    return f"میو فعال شد ✅ (هر {shown:g} دقیقه)"


async def untoggle_meow(chat_id: int) -> str:
    task = active_tasks.pop(chat_id, None)
    if task:
        task.cancel()
        return "میو غیرفعال شد ❌"
    return "میو تو این گپ فعال نبود"


async def toggle_afk(custom_message: str = "") -> str:
    global afk_enabled, afk_message
    if custom_message:
        afk_message = custom_message
    afk_enabled = True
    afk_replied_chats.clear()
    return f"حالت افک فعال شد ✅\nپیام: {afk_message}"


async def untoggle_afk() -> str:
    global afk_enabled
    afk_enabled = False
    afk_replied_chats.clear()
    return "حالت افک غیرفعال شد ❌ خوش اومدی 👋"


async def toggle_clock_bio() -> str:
    global clock_bio_task
    if clock_bio_task:
        return "ساعت بیو از قبل فعال بود 🕐"
    clock_bio_task = asyncio.create_task(clock_bio_loop())
    return f"ساعت خودکار بیو فعال شد ✅ (هر {clock_interval_seconds} ثانیه)"


async def untoggle_clock_bio() -> str:
    global clock_bio_task
    if clock_bio_task:
        clock_bio_task.cancel()
        clock_bio_task = None
        return "ساعت بیو غیرفعال شد ❌"
    return "ساعت بیو فعال نبود"


async def toggle_clock_name() -> str:
    global clock_name_task
    if clock_name_task:
        return "ساعت اسم از قبل فعال بود 🕐"
    clock_name_task = asyncio.create_task(clock_name_loop())
    return f"ساعت خودکار نام خانوادگی فعال شد ✅ (هر {clock_interval_seconds} ثانیه)"


async def untoggle_clock_name() -> str:
    global clock_name_task
    if clock_name_task:
        clock_name_task.cancel()
        clock_name_task = None
        return "ساعت اسم غیرفعال شد ❌"
    return "ساعت اسم فعال نبود"


# ---------- فارم خودکار بات میویی (یا هر بات مشابه با پیام + دکمه شیشه‌ای) ----------
async def meowie_farm_once():
    """یه‌بار پیام محرک رو می‌فرسته و روی دکمه‌ی برداشت کلیک می‌کنه"""
    async with client.conversation(MEOWIE_BOT_USERNAME, timeout=30) as conv:
        await conv.send_message(MEOWIE_TRIGGER_TEXT)
        response = await conv.get_response()
        await asyncio.sleep(1)  # یه مکث کوچیک قبل از کلیک، شبیه‌تر به رفتار انسانی
        await response.click(text=lambda t: t and MEOWIE_BUTTON_KEYWORD in t)


async def farm_loop():
    try:
        while True:
            try:
                await meowie_farm_once()
            except Exception as e:
                print(f"خطا توی فارم میویی: {e}")
            await asyncio.sleep(MEOWIE_FARM_INTERVAL_SECONDS)
    except asyncio.CancelledError:
        pass


async def toggle_farm() -> str:
    global farm_task
    if farm_task:
        return "فارم میویی از قبل فعال بود 🐱"
    farm_task = asyncio.create_task(farm_loop())
    minutes = MEOWIE_FARM_INTERVAL_SECONDS / 60
    return f"فارم میویی فعال شد ✅ (هر {minutes:g} دقیقه)"


async def untoggle_farm() -> str:
    global farm_task
    if farm_task:
        farm_task.cancel()
        farm_task = None
        return "فارم میویی غیرفعال شد ❌"
    return "فارم میویی فعال نبود"


# ---------- توابع کمکی شبکه‌ای (اجرا در thread جدا تا event loop بلاک نشه) ----------
def _shorten_url_sync(url: str) -> str:
    api = "https://tinyurl.com/api-create.php?" + urllib.parse.urlencode({"url": url})
    with urllib.request.urlopen(api, timeout=10) as resp:
        return resp.read().decode("utf-8")


async def shorten_url(url: str) -> str:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, _shorten_url_sync, url)


def _translate_sync(text: str, source: str, target: str) -> str:
    params = urllib.parse.urlencode({"q": text, "langpair": f"{source}|{target}"})
    api = f"https://api.mymemory.translated.net/get?{params}"
    with urllib.request.urlopen(api, timeout=10) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["responseData"]["translatedText"]


async def translate_text(text: str) -> str:
    # اگه بیشتر حروف فارسی بود، فارسی به انگلیسی، وگرنه برعکس
    persian_chars = sum(1 for ch in text if "\u0600" <= ch <= "\u06FF")
    source, target = ("fa", "en") if persian_chars > len(text) / 2 else ("en", "fa")
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, _translate_sync, text, source, target)


# ---------- ۱) میو دوره‌ای ----------
async def meow_loop(chat_id: int, seconds: float | None = None):
    wait = seconds if seconds else interval_seconds
    try:
        while True:
            await asyncio.sleep(wait)
            await client.send_message(chat_id, "میو")
    except asyncio.CancelledError:
        pass


def fancy_time() -> str:
    """ساعت رو با فونت یونیکد شیک (دابل-استرایک) برمی‌گردونه"""
    return convert_font(now_str(), FONT_MAPS["𝕯𝖔𝖚𝖇𝖑𝖊"])


# ---------- ۲) ساعت خودکار در بیو ----------
async def clock_bio_loop():
    try:
        while True:
            await client(UpdateProfileRequest(about=f"🕐 {fancy_time()}"))
            await asyncio.sleep(clock_interval_seconds)
    except asyncio.CancelledError:
        pass


# ---------- ۳) ساعت خودکار در نام خانوادگی ----------
async def clock_name_loop():
    try:
        while True:
            await client(UpdateProfileRequest(last_name=f"🕐 {fancy_time()}"))
            await asyncio.sleep(clock_interval_seconds)
    except asyncio.CancelledError:
        pass


# ---------- ۴) فونت‌ساز یونیکد ----------
FONT_MAPS = {
    "𝐁𝐨𝐥𝐝": {
        **{c: chr(0x1D400 + i) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")},
        **{c: chr(0x1D41A + i) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")},
        **{c: chr(0x1D7CE + i) for i, c in enumerate("0123456789")},
    },
    "𝑰𝒕𝒂𝒍𝒊𝒄": {
        **{c: chr(0x1D434 + i) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")},
        **{c: chr(0x1D44E + i) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")},
    },
    "𝓢𝓬𝓻𝓲𝓹𝓽": {
        **{c: chr(0x1D4D0 + i) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")},
        **{c: chr(0x1D4EA + i) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")},
    },
    "𝔉𝔯𝔞𝔨𝔱𝔲𝔯": {
        **{c: chr(0x1D504 + i) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")},
        **{c: chr(0x1D51E + i) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")},
    },
    "𝕯𝖔𝖚𝖇𝖑𝖊": {
        **{c: chr(0x1D538 + i) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")},
        **{c: chr(0x1D552 + i) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")},
        **{c: chr(0x1D7D8 + i) for i, c in enumerate("0123456789")},
    },
    "Ⓒⓘⓡⓒⓛⓔ": {
        **{c: chr(0x24B6 + i) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")},
        **{c: chr(0x24D0 + i) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")},
    },
    "𝙼𝚘𝚗𝚘": {
        **{c: chr(0x1D670 + i) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")},
        **{c: chr(0x1D68A + i) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")},
        **{c: chr(0x1D7F6 + i) for i, c in enumerate("0123456789")},
    },
    "𝑩𝒐𝒍𝒅𝑰𝒕𝒂𝒍𝒊𝒄": {
        **{c: chr(0x1D468 + i) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")},
        **{c: chr(0x1D482 + i) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")},
    },
    "𝖲𝖺𝗇𝗌": {
        **{c: chr(0x1D5A0 + i) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")},
        **{c: chr(0x1D5BA + i) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")},
        **{c: chr(0x1D7E2 + i) for i, c in enumerate("0123456789")},
    },
    "𝗦𝗮𝗻𝘀𝗕𝗼𝗹𝗱": {
        **{c: chr(0x1D5D4 + i) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")},
        **{c: chr(0x1D5EE + i) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")},
        **{c: chr(0x1D7EC + i) for i, c in enumerate("0123456789")},
    },
    "𝘚𝘢𝘯𝘴𝘐𝘵𝘢𝘭𝘪𝘤": {
        **{c: chr(0x1D608 + i) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")},
        **{c: chr(0x1D622 + i) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")},
    },
    "𝕭𝖔𝖑𝖉𝕱𝖗𝖆𝖐𝖙𝖚𝖗": {
        **{c: chr(0x1D56C + i) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")},
        **{c: chr(0x1D586 + i) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")},
    },
    "Ｆｕｌｌｗｉｄｔｈ": {
        **{c: chr(0xFF21 + i) for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")},
        **{c: chr(0xFF41 + i) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")},
        **{c: chr(0xFF10 + i) for i, c in enumerate("0123456789")},
    },
    "sᴍᴀʟʟ ᴄᴀᴘs": {
        **dict(zip(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ",
        )),
        **dict(zip(
            "abcdefghijklmnopqrstuvwxyz",
            "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ",
        )),
    },
}

# اسم‌های ساده (فارسی/انگلیسی) برای انتخاب یه سبک خاص در دستور «اسم فونت»
FONT_ALIASES = {
    "bold": "𝐁𝐨𝐥𝐝", "بولد": "𝐁𝐨𝐥𝐝",
    "italic": "𝑰𝒕𝒂𝒍𝒊𝒄", "ایتالیک": "𝑰𝒕𝒂𝒍𝒊𝒄",
    "script": "𝓢𝓬𝓻𝓲𝓹𝓽", "اسکریپت": "𝓢𝓬𝓻𝓲𝓹𝓽",
    "fraktur": "𝔉𝔯𝔞𝔨𝔱𝔲𝔯", "فراکتور": "𝔉𝔯𝔞𝔨𝔱𝔲𝔯",
    "double": "𝕯𝖔𝖚𝖇𝖑𝖊", "دابل": "𝕯𝖔𝖚𝖇𝖑𝖊",
    "circle": "Ⓒⓘⓡⓒⓛⓔ", "دایره": "Ⓒⓘⓡⓒⓛⓔ",
    "mono": "𝙼𝚘𝚗𝚘", "مونو": "𝙼𝚘𝚗𝚘",
    "bolditalic": "𝑩𝒐𝒍𝒅𝑰𝒕𝒂𝒍𝒊𝒄", "بولدایتالیک": "𝑩𝒐𝒍𝒅𝑰𝒕𝒂𝒍𝒊𝒄",
    "sans": "𝖲𝖺𝗇𝗌", "سنس": "𝖲𝖺𝗇𝗌",
    "sansbold": "𝗦𝗮𝗻𝘀𝗕𝗼𝗹𝗱", "سنسبولد": "𝗦𝗮𝗻𝘀𝗕𝗼𝗹𝗱",
    "sansitalic": "𝘚𝘢𝘯𝘴𝘐𝘵𝘢𝘭𝘪𝘤", "سنسایتالیک": "𝘚𝘢𝘯𝘴𝘐𝘵𝘢𝘭𝘪𝘤",
    "boldfraktur": "𝕭𝖔𝖑𝖉𝕱𝖗𝖆𝖐𝖙𝖚𝖗", "بولدفراکتور": "𝕭𝖔𝖑𝖉𝕱𝖗𝖆𝖐𝖙𝖚𝖗",
    "fullwidth": "Ｆｕｌｌｗｉｄｔｈ", "فول‌ویدث": "Ｆｕｌｌｗｉｄｔｈ",
    "smallcaps": "sᴍᴀʟʟ ᴄᴀᴘs", "اسمالکپس": "sᴍᴀʟʟ ᴄᴀᴘs",
}


def convert_font(text: str, mapping: dict) -> str:
    return "".join(mapping.get(ch, ch) for ch in text)


# ---------- ۵) ماشین‌حساب امن ----------
_SAFE_OPS = {
    ast.Add: operator.add, ast.Sub: operator.sub,
    ast.Mult: operator.mul, ast.Div: operator.truediv,
    ast.Pow: operator.pow, ast.Mod: operator.mod,
    ast.USub: operator.neg, ast.UAdd: operator.pos,
    ast.FloorDiv: operator.floordiv,
}


def safe_eval(expr: str):
    """فقط عملیات ریاضی ساده رو محاسبه می‌کنه، بدون اجرای کد دلخواه"""
    def _eval(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in _SAFE_OPS:
            return _SAFE_OPS[type(node.op)](_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in _SAFE_OPS:
            return _SAFE_OPS[type(node.op)](_eval(node.operand))
        raise ValueError("عبارت نامعتبر")

    tree = ast.parse(expr, mode="eval")
    return _eval(tree.body)


# ---------- هندلر اصلی ----------
@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    global bot_enabled, markread_private_enabled, markread_group_enabled

    text = event.raw_text.strip()
    chat_id = event.chat_id

    # --- سوییچ کلی روشن/خاموش ---
    if text == "ربات روشن":
        bot_enabled = True
        await event.edit("ربات روشن شد ✅")
        return
    elif text == "ربات خاموش":
        bot_enabled = False
        await event.edit("ربات خاموش شد ❌ (فقط همین دستور کار می‌کنه)")
        return
    if not bot_enabled:
        return

    # --- میو ---
    if text == "میو فعال":
        await event.reply(await toggle_meow(chat_id))

    elif text == "میو غیرفعال":
        await event.reply(await untoggle_meow(chat_id))

    # --- ساعت خودکار در بیو ---
    elif text == "ساعت بیو فعال":
        await event.reply(await toggle_clock_bio())

    elif text == "ساعت بیو غیرفعال":
        await event.reply(await untoggle_clock_bio())

    # --- ساعت خودکار در نام خانوادگی ---
    elif text == "ساعت اسم فعال":
        await event.reply(await toggle_clock_name())

    elif text == "ساعت اسم غیرفعال":
        await event.reply(await untoggle_clock_name())

    # --- فونت‌ساز ---
    elif text.startswith(".فونت "):
        raw = text[len(".فونت "):].strip()
        if not raw:
            await event.reply("بعد از «.فونت» یه متن (انگلیسی) بنویس. مثال: .فونت Hello")
            return
        lines = [f"{name}: {convert_font(raw, mapping)}" for name, mapping in FONT_MAPS.items()]
        await event.edit("\n".join(lines))

    # --- گذاشتن اسم پروفایل با یه سبک فونت خاص ---
    elif text.startswith("اسم فونت "):
        rest = text[len("اسم فونت "):].strip()
        parts = rest.split(" ", 1)
        if len(parts) < 2:
            style_list = ", ".join(sorted(set(FONT_ALIASES.keys())))
            await event.edit(f"مثال درست: اسم فونت Sans Mohammad\nسبک‌های موجود: {style_list}")
            return
        style_key, name_text = parts[0].lower(), parts[1].strip()
        mapping_key = FONT_ALIASES.get(style_key)
        if not mapping_key:
            style_list = ", ".join(sorted(set(FONT_ALIASES.keys())))
            await event.edit(f"سبک ناشناخته. سبک‌های موجود: {style_list}")
            return
        new_name = convert_font(name_text, FONT_MAPS[mapping_key])
        await client(UpdateProfileRequest(first_name=new_name))
        await event.edit(f"اسم پروفایل تغییر کرد ✅\n{new_name}")

    # --- پینگ ---
    elif text == ".پینگ":
        start = datetime.now()
        msg = await event.edit("در حال سنجش...")
        delta = (datetime.now() - start).total_seconds() * 1000
        await msg.edit(f"پونگ! 🏓 {delta:.0f} ms")

    # --- حالت افک (دور از دسترس) ---
    elif text.startswith("افک فعال"):
        custom = text[len("افک فعال"):].strip()
        await event.edit(await toggle_afk(custom))

    elif text == "افک غیرفعال":
        await event.edit(await untoggle_afk())

    # --- آیدی (چت فعلی یا کاربر ریپلای‌شده) ---
    elif text == ".آیدی":
        if event.is_reply:
            reply_msg = await event.get_reply_message()
            sender = await reply_msg.get_sender()
            uid = sender.id if sender else "نامشخص"
            await event.edit(f"آیدی این کاربر: `{uid}`")
        else:
            await event.edit(f"آیدی این گپ: `{chat_id}`")

    # --- اطلاعات کاربر ریپلای‌شده ---
    elif text == ".اطلاعات":
        if not event.is_reply:
            await event.edit("باید روی پیام یه کاربر ریپلای بزنی")
            return
        reply_msg = await event.get_reply_message()
        sender = await reply_msg.get_sender()
        if not sender:
            await event.edit("کاربر پیدا نشد")
            return
        full = await client(GetFullUserRequest(sender.id))
        bio = full.full_user.about or "—"
        name = f"{sender.first_name or ''} {sender.last_name or ''}".strip()
        username = f"@{sender.username}" if sender.username else "—"
        info = (
            f"👤 اطلاعات کاربر\n"
            f"نام: {name}\n"
            f"یوزرنیم: {username}\n"
            f"آیدی: `{sender.id}`\n"
            f"بیو: {bio}"
        )
        await event.edit(info)

    # --- پاک کردن n پیام آخر خودت توی این گپ ---
    elif text.startswith(".پاک "):
        count_str = text[len(".پاک "):].strip()
        if not count_str.isdigit():
            await event.edit("مثال درست: .پاک 10")
            return
        count = min(int(count_str), 100)  # سقف ۱۰۰ برای جلوگیری از ریسک فلود
        await event.delete()  # خود دستور رو هم پاک کن
        ids_to_delete = []
        async for m in client.iter_messages(chat_id, from_user="me", limit=count):
            ids_to_delete.append(m.id)
        if ids_to_delete:
            await client.delete_messages(chat_id, ids_to_delete)

    # --- ماشین‌حساب ---
    elif text.startswith(".حساب "):
        expr = text[len(".حساب "):].strip()
        try:
            result = safe_eval(expr)
            await event.edit(f"🧮 {expr} = {result}")
        except Exception:
            await event.edit("عبارت نامعتبره. مثال: .حساب (5+3)*2")

    # --- پیام خودتخریب‌شونده: .حذف <ثانیه> <متن> ---
    elif text.startswith(".حذف "):
        parts = text[len(".حذف "):].strip().split(" ", 1)
        if len(parts) < 2 or not parts[0].isdigit():
            await event.edit("مثال درست: .حذف 10 این پیام بعد ۱۰ ثانیه پاک میشه")
            return
        seconds = min(int(parts[0]), 3600)  # سقف یک ساعت
        content = parts[1]
        msg = await event.edit(content)
        await asyncio.sleep(seconds)
        await msg.delete()

    # --- شبیه‌سازی تایپ قبل از ارسال: .تایپ <متن> ---
    elif text.startswith(".تایپ "):
        content = text[len(".تایپ "):].strip()
        await event.delete()
        async with client.action(chat_id, "typing"):
            # مدت تایپ متناسب با طول متن (حداکثر ۵ ثانیه)
            await asyncio.sleep(min(len(content) * 0.05, 5))
        await client.send_message(chat_id, content)

    # --- آمار گپ‌ها ---
    elif text == ".آمار":
        groups = channels = users = 0
        async for d in client.iter_dialogs():
            if d.is_group:
                groups += 1
            elif d.is_channel:
                channels += 1
            elif d.is_user:
                users += 1
        await event.edit(f"📊 آمار\nگروه‌ها: {groups}\nکانال‌ها: {channels}\nچت‌های خصوصی: {users}")

    # --- حالت خوانده‌شدن خودکار (جدا برای پیوی و گروه) ---
    elif text == "خوانده‌شدن پیوی فعال":
        markread_private_enabled = True
        await event.edit("خوانده‌شدن خودکار پیوی فعال شد ✅")

    elif text == "خوانده‌شدن پیوی غیرفعال":
        markread_private_enabled = False
        await event.edit("خوانده‌شدن خودکار پیوی غیرفعال شد ❌")

    elif text == "خوانده‌شدن گروه فعال":
        markread_group_enabled = True
        await event.edit("خوانده‌شدن خودکار گروه فعال شد ✅")

    elif text == "خوانده‌شدن گروه غیرفعال":
        markread_group_enabled = False
        await event.edit("خوانده‌شدن خودکار گروه غیرفعال شد ❌")

    # --- لیست نشست‌های فعال اکانت ---
    elif text == ".نشست‌ها":
        result = await client(GetAuthorizationsRequest())
        lines = ["🔐 نشست‌های فعال:"]
        for auth in result.authorizations:
            flag = "⭐️ (همین دستگاه)" if auth.current else ""
            lines.append(f"- {auth.device_model} / {auth.platform} {flag}")
        await event.edit("\n".join(lines))

    # --- ذخیره پیام ریپلای‌شده در سیو مسیجز ---
    elif text == ".ذخیره":
        if not event.is_reply:
            await event.edit("باید روی یه پیام ریپلای بزنی")
            return
        reply_msg = await event.get_reply_message()
        await client.forward_messages("me", reply_msg)
        await event.edit("توی سیو مسیجز ذخیره شد ✅")

    # --- بلاک / آنبلاک کاربر ریپلای‌شده ---
    elif text == ".بلاک":
        if not event.is_reply:
            await event.edit("باید روی پیام یه کاربر ریپلای بزنی")
            return
        sender = await (await event.get_reply_message()).get_sender()
        await client(BlockRequest(sender.id))
        await event.edit(f"کاربر {sender.id} بلاک شد 🚫")

    elif text == ".آنبلاک":
        if not event.is_reply:
            await event.edit("باید روی پیام یه کاربر ریپلای بزنی")
            return
        sender = await (await event.get_reply_message()).get_sender()
        await client(UnblockRequest(sender.id))
        await event.edit(f"کاربر {sender.id} آنبلاک شد ✅")

    # --- کوتاه‌کننده لینک ---
    elif text.startswith(".کوتاه "):
        url = text[len(".کوتاه "):].strip()
        try:
            short = await shorten_url(url)
            await event.edit(f"🔗 {short}")
        except Exception:
            await event.edit("خطا توی کوتاه کردن لینک. لینک رو چک کن.")

    # --- ساعت منطقه‌ای ---
    elif text.startswith(".ساعت "):
        zone_key = text[len(".ساعت "):].strip().lower()
        tz_name = TIMEZONES.get(zone_key)
        if not tz_name:
            zones = "، ".join(sorted(set(TIMEZONES.keys())))
            await event.edit(f"منطقه ناشناخته. گزینه‌ها: {zones}")
            return
        now = datetime.now(ZoneInfo(tz_name))
        await event.edit(f"🕐 {zone_key}: {now.strftime('%H:%M:%S - %Y/%m/%d')}")

    # --- ترجمه ---
    elif text.startswith(".ترجمه "):
        content = text[len(".ترجمه "):].strip()
        try:
            translated = await translate_text(content)
            await event.edit(f"🌐 {translated}")
        except Exception:
            await event.edit("خطا توی ترجمه. دوباره امتحان کن.")

    # --- مدیریت پاسخ سریع ---
    elif text.startswith(".پاسخ‌سریع تنظیم "):
        rest = text[len(".پاسخ‌سریع تنظیم "):]
        if "|" not in rest:
            await event.edit("مثال درست: .پاسخ‌سریع تنظیم سلام | چطوری؟")
            return
        trigger, answer = rest.split("|", 1)
        quick_replies[trigger.strip().lower()] = answer.strip()
        await event.edit(f"پاسخ سریع برای «{trigger.strip()}» ذخیره شد ✅")

    elif text.startswith(".پاسخ‌سریع حذف "):
        trigger = text[len(".پاسخ‌سریع حذف "):].strip().lower()
        if quick_replies.pop(trigger, None) is not None:
            await event.edit(f"پاسخ سریع «{trigger}» حذف شد ❌")
        else:
            await event.edit("همچین پاسخ سریعی وجود نداشت")

    elif text == ".پاسخ‌سریع پاک":
        quick_replies.clear()
        await event.edit("همه‌ی پاسخ‌های سریع پاک شدن ❌")

    elif text == ".پاسخ‌سریع لیست":
        if not quick_replies:
            await event.edit("هیچ پاسخ سریعی تنظیم نشده")
            return
        lines = [f"- {k} → {v}" for k, v in quick_replies.items()]
        await event.edit("📋 پاسخ‌های سریع:\n" + "\n".join(lines))

    # --- راهنما ---
    elif text in (".راهنما", "راهنما"):
        await event.edit(HELP_TEXT)

    # --- فارم خودکار بات میویی ---
    elif text == "فارم میویی فعال":
        await event.edit(await toggle_farm())

    elif text == "فارم میویی غیرفعال":
        await event.edit(await untoggle_farm())


@client.on(events.NewMessage(incoming=True))
async def incoming_watcher(event):
    """
    این هندلر دو کار انجام می‌ده:
    ۱) اگه افک فعال باشه، به اولین پیام خصوصی هر کاربر یه بار جواب خودکار می‌ده
    ۲) دستورهای اکانت(های) مدیر (ADMIN_IDS) رو پردازش می‌کنه
    """
    sender_id = event.sender_id
    text = (event.raw_text or "").strip()

    # --- ۲.۱) حذف پیام از راه دور: مدیر روی پیام خودِ اکانت ریپلای می‌زنه و می‌نویسه «پاک» ---
    if event.is_reply and text == "پاک" and sender_id in ADMIN_IDS:
        reply_msg = await event.get_reply_message()
        if reply_msg and reply_msg.out:  # یعنی پیام قبلی رو خودِ همین اکانت فرستاده
            await reply_msg.delete()
            await event.delete()  # پیام «پاک» مدیر رو هم پاک کن
        return

    # --- ۲.۲) کنترل از راه دور: مدیر توی پیوی خودِ همین اکانت دستور می‌فرسته ---
    if event.is_private and sender_id in ADMIN_IDS:
        admin_chat_id = event.chat_id

        # --- گام دوم: منتظر آیدی/لینک گروه بودیم ---
        if sender_id in admin_awaiting_group:
            admin_awaiting_group.discard(sender_id)
            parts = text.split()
            target_raw = parts[0] if parts else ""
            minutes = None
            if len(parts) >= 2:
                try:
                    minutes = float(parts[1])
                except ValueError:
                    minutes = None

            try:
                if target_raw.lstrip("-").isdigit():
                    target_chat_id = int(target_raw)
                else:
                    entity = await client.get_entity(target_raw)
                    target_chat_id = entity.id
                msg = await toggle_meow(target_chat_id, minutes)
                await event.reply(f"گروه شناسایی شد ✅\n{msg}")
            except Exception:
                await event.reply(
                    "نتونستم این گروه رو شناسایی کنم. مطمئن شو آیدی عددی درسته یا "
                    "لینک عمومیه، یا اینکه اکانت اصلی از قبل عضو اون گروهه."
                )
            return

        if text.lower() == "mio online is gp":
            admin_awaiting_group.add(sender_id)
            await event.reply(
                "آیدی عددی گروه یا لینک عمومی‌ش رو بفرست.\n"
                "اگه می‌خوای فاصله‌ی زمانی هم غیر از پیش‌فرض باشه، بعدش یه فاصله بذار و عدد دقیقه رو بنویس.\n"
                "مثال: -1001234567890 5"
            )
            return

        if text in (".راهنما", "راهنما"):
            await event.reply(HELP_TEXT)
            return

        if text == ".پینگ":
            start = datetime.now()
            msg = await event.reply("در حال سنجش...")
            delta = (datetime.now() - start).total_seconds() * 1000
            await msg.edit(f"پونگ! 🏓 {delta:.0f} ms")
            return

        if text.startswith("میو فعال"):
            rest = text[len("میو فعال"):].strip()
            minutes = None
            if rest:
                try:
                    minutes = float(rest)
                except ValueError:
                    await event.reply("عدد دقیقه نامعتبره. مثال: میو فعال 5")
                    return
            await event.reply(await toggle_meow(admin_chat_id, minutes))
            return
        elif text == "میو غیرفعال":
            await event.reply(await untoggle_meow(admin_chat_id))
            return
        elif text.startswith("افک فعال"):
            custom = text[len("افک فعال"):].strip()
            await event.reply(await toggle_afk(custom))
            return
        elif text == "افک غیرفعال":
            await event.reply(await untoggle_afk())
            return
        elif text == "ساعت بیو فعال":
            await event.reply(await toggle_clock_bio())
            return
        elif text == "ساعت بیو غیرفعال":
            await event.reply(await untoggle_clock_bio())
            return
        elif text == "ساعت اسم فعال":
            await event.reply(await toggle_clock_name())
            return
        elif text == "ساعت اسم غیرفعال":
            await event.reply(await untoggle_clock_name())
            return

    # --- خوانده‌شدن خودکار (جدا برای پیوی و گروه) ---
    should_mark_read = (
        (event.is_private and markread_private_enabled)
        or (event.is_group and markread_group_enabled)
    )
    if should_mark_read:
        try:
            await client.send_read_acknowledge(event.chat_id, event.message)
        except Exception:
            pass

    # --- پاسخ سریع (کلمه‌کلیدی) ---
    trigger = text.lower()
    if trigger in quick_replies:
        await event.reply(quick_replies[trigger])
        return

    # --- ۱) پاسخ خودکار افک ---
    if not afk_enabled:
        return
    if not event.is_private:
        return
    chat_id = event.chat_id
    if chat_id in afk_replied_chats:
        return
    afk_replied_chats.add(chat_id)
    await event.reply(afk_message)


async def main():
    await client.start()
    print("سلف‌بات اجرا شد. دستورات:")
    print("  میو فعال / میو غیرفعال")
    print("  ساعت بیو فعال / ساعت بیو غیرفعال")
    print("  ساعت اسم فعال / ساعت اسم غیرفعال")
    print("  .فونت <متن>")
    print("  اسم فونت <سبک> <متن>")
    print("  .پینگ")
    print("  افک فعال <پیام> / افک غیرفعال")
    print("  .آیدی")
    print("  .اطلاعات (روی ریپلای)")
    print("  .پاک <عدد>")
    print("  .حساب <عبارت>")
    print("  .حذف <ثانیه> <متن>")
    print("  .تایپ <متن>")
    print("  ربات روشن / ربات خاموش")
    print("  .آمار | خوانده‌شدن پیوی/گروه فعال یا غیرفعال | .نشست‌ها | .ذخیره")
    print("  .بلاک / .آنبلاک (روی ریپلای) | .کوتاه <لینک> | .ساعت <منطقه>")
    print("  .ترجمه <متن> | .پاسخ‌سریع تنظیم/حذف/پاک/لیست | .راهنما")
    print("  فارم میویی فعال / فارم میویی غیرفعال")
    if ADMIN_IDS:
        print(f"  کنترل مدیریتی برای {len(ADMIN_IDS)} اکانت مدیر فعاله (پیوی + حذف با ریپلای «پاک»)")
    else:
        print("  ⚠️ ADMIN_IDS خالیه — قابلیت مدیریتی غیرفعاله تا آیدی مدیر رو اضافه کنی")
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
