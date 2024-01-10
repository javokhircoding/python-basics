from transliterate import to_cyrillic, to_latin  #krch kayp
import telebot

TOKEN = "6845457979:AAG1EfhRjvF8WqeBOF6Udrk4SQcAf59Abd"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu Alaykum, Xush kelibsiz!")


bot.polling()

#matn = input("Matn kiriting: ")

#if matn.isascii():
#    print(to_cyrillic(matn))
#else:
#    print(to_latin(matn))