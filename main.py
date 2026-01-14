import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from openai import OpenAI

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Sen o‘zbek tilida gapiradigan aqlli yordamchisan.\n{user_text}"
    )

    await update.message.reply_text(response.output_text)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
app.run_polling()

