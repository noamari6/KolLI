from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from config import TELEGRAM_TOKEN
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("שלח לי הקלטת קול (voice), ואחר כך טקסט – ואחזיר לך הקראה.")

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    file = await update.message.voice.get_file()
    os.makedirs("voices", exist_ok=True)
    voice_path = f"voices/{user_id}.ogg"
    await file.download_to_drive(voice_path)
    await update.message.reply_text("קיבלתי את ההקלטה! עכשיו תשלח לי טקסט.")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("הקראה תעבוד בשלב הבא. כרגע רק מאחסן קול וטקסט.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_text))
    app.run_polling()
