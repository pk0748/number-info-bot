import requests
import telebot

TOKEN = "8210964572:AAFbIhAcDs7Sc7ve2uBLLNFxB08hDPjFsUw"
API = "https://fuck.proportalxc.workers.dev/?num="

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "👋 Welcome\n\nNumber info ke liye likho:\n/num 9876543210"
    )

@bot.message_handler(commands=['num'])
def num(message):
    try:
        parts = message.text.split()
        if len(parts) < 2:
            bot.reply_to(message, "❌ /num 9876543210")
            return

        raw = "".join(parts[1:])
        number = "".join(c for c in raw if c.isdigit())

        if len(number) != 10:
            bot.reply_to(message, "❌ Sirf 10 digit number bhejo")
            return

        r = requests.get(API + number, timeout=10)
        bot.reply_to(message, r.text)

    except Exception as e:
        bot.reply_to(message, "⚠️ API error")

print("🤖 Bot running...")
bot.infinity_polling()
