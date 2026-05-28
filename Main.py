import os
import telebot
from openai import OpenAI

TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "VOLOHA CORE ONLINE")

@bot.message_handler(func=lambda message: True)
def chat(message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": message.text}
        ]
    )

    answer = response.choices[0].message.content
    bot.reply_to(message, answer)

bot.infinity_polling()
