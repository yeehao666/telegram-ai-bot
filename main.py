import telebot
import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def ask_ai(text):
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-70b-versatile",
            "messages": [
                {"role": "system", "content": "Ты дружелюбный ассистент."},
                {"role": "user", "content": text}
            ]
        }
    )
    return response.json()["choices"][0]["message"]["content"]

@bot.message_handler(func=lambda message: True)
def handle(message):
    bot.send_message(message.chat.id, ask_ai(message.text))

print("Bot started...")
bot.polling()
