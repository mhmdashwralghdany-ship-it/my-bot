
import random, json, os, requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import json

BOT_TOKEN = os.getenv("BOT_TOKEN")


Your token was replaced with a new one. You can use this token to access HTTP API:
8854506215:
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت شغال!")

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

def load_top():
    if os.path.exists("top.json"):
        with open("top.json", 'r') as f: return json.load(f)
    return {}
def save_top(data):
    with open("top.json", 'w') as f: json.dump(data, f)
def add_point(user_id, name):
    data = load_top()
    if str(user_id) not in data: data[str(user_id)] = {"name": name, "score": 0}
    data[str(user_id)]["score"] += 1
    save_top(data)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    add_point(update.effective_user.id, update.effective_user.first_name)
    await update.message.reply_text(f"أهلا {update.effective_user.first_name} 👑\nالبوت شغال دايم 24ساعة\n/help للاوامر")

async def help_cmd(update, context):
    await update.message.reply_text("/zakhrafa + اسمك\n/sarah\n/nokta\n/suwar\n/quran\n/top")

async def zakhrafa(update, context):
    name = " ".join(context.args) if context.args else update.effective_user.first_name
    await update.message.reply_text(f"꧁༒ {name} ༒꧂ 👑")

async def sarah_cmd(update, context):
    await update.message.reply_text(random.choice(["لو بتحبي حد هتقولي ايه؟", "اكتر حاجة جريئة عملتيها؟", "بتثقي بسرعة؟"]))

async def nokta_cmd(update, context):
    await update.message.reply_text(random.choice(["مرة واحد راح للدكتور قاله عيني بتوجعني لما اشرب شاي قاله شيل المعلقة 😂", "واحد نام متأخر صحي لقى النوم خلص 😂"]))

async def suwar_cmd(update, context):
    await update.message.reply_photo(f"https://picsum.photos/600/400?random={random.randint(1,99999)}")

async def quran_cmd(update, context):
    try:
        r = requests.get("https://api.alquran.cloud/v1/ayah/random/ar.asad", timeout=10).json()
        await update.message.reply_text(f"﴿ {r['data']['text']} ﴾\n- {r['data']['surah']['name']} ❤️")
    except:
        await update.message.reply_text("﴿ وَمَن يَتَّقِ اللَّهَ يَجْعَل لَّهُ مَخْرَجًا ﴾")

async def top_cmd(update, context):
    data = load_top()
    txt = "🏆 الترتيب:\n"
    for i, u in enumerate(sorted(data.values(), key=lambda x: x['score'], reverse=True)[:10], 1):
        txt += f"{i}. {u['name']} - {u['score']}\n"
    await update.message.reply_text(txt)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(CommandHandler("zakhrafa", zakhrafa))
app.add_handler(CommandHandler("sarah", sarah_cmd))
app.add_handler(CommandHandler("fadfada", sarah_cmd))
app.add_handler(CommandHandler("nokta", nokta_cmd))
app.add_handler(CommandHandler("suwar", suwar_cmd))
app.add_handler(CommandHandler("search", suwar_cmd))
app.add_handler(CommandHandler("quran", quran_cmd))
app.add_handler(CommandHandler("top", top_cmd))
app.run_polling()
