import telebot

# Создайте экземпляр бота
bot = telebot.TeleBot(token)

# Обработчик сообщений
@bot.message_handler(commands=["start"])
def start(message):
    # Отправьте сообщение пользователю
    bot.send_message(message.chat.id, "Привет!")

# Запустите бота
bot.polling()
