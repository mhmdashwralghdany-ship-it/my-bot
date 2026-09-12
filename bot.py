import random, json, os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

def load_top():
    if os.path.exists("top.json"):
        with open("top.json", 'r') as f: 
            return json.load(f)
    return {}

def save_top(data):
    with open("top.json", 'w') as f: 
        json.dump(data, f)

def add_point(user_id, name):
    data = load_top()
    if str(user_id) not in data: 
        data[str(user_id)] = {"name": name, "score": 0}
    data[str(user_id)]["score"] += 1
    save_top(data)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    add_point(update.effective_user.id, update.effective_user.first_name)
    await update.message.reply_text(f"اهلا {update.effective_user.first_name} 👑 البوت شغال دايم 24 ساعة")

async def help_cmd(update, context):
    await update.message.reply_text("/zakhrafa + اسمك\n/sarah\n/nokta\n/suwar\n/quran\n/top")

async def zakhrafa(update, context):
    name = " ".join(context.args) if context.args else update.effective_user.first_name
    await update.message.reply_text(f"✨ {name} ✨👑")

async def sarah_cmd(update, context):
    await update.message.reply_text(random.choice(["بسرعة", "اكتر حاجة جريئة عملتيها؟", "حد هتقولي ايه؟"]))

async def fadfada(update, context):
    await update.message.reply_text(random.choice(["سامعك ❤️ احكي", "فضفض براحتك", "انا هنا اسمعك"]))

async def xo(update, context):
    await update.message.reply_text("X O لسه بنظبطها 🎮")

async def nokta(update, context):
    await update.message.reply_text(random.choice(["مرة واحد...", "نكتة جامدة 😂"]))

async def top_cmd(update, context):
    data = load_top()
    if not data:
        await update.message.reply_text("لسه مفيش نقط")
        return
    txt = "\n".join([f"{v['name']}: {v['score']}" for v in data.values()])
    await update.message.reply_text(f"التوب:\n{txt}")

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("zakhrafa", zakhrafa))
    app.add_handler(CommandHandler("sarah", sarah_cmd))
    app.add_handler(CommandHandler("fadfada", fadfada))
    app.add_handler(CommandHandler("xo", xo))
    app.add_handler(CommandHandler("nokta", nokta))
    app.add_handler(CommandHandler("top", top_cmd))
    app.run_polling(drop_pending_updates=True)
