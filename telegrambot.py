import telebot

TOKEN = "6241515749:AAF94ZSTzPhhCUUaV8S_Vahj3BSqyg7yHjM"

bot = telebot.TeleBot(TOKEN)

bot.polling(none_stop=True)

@bot.message_handler(filters)
def function_name(message):
    bot.reply_to(message, "This is a message handler")
