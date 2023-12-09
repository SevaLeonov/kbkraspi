import telebot
import pandas as pd

# Инициализируем бота
bot = telebot.TeleBot("6613694276:AAEWBo_Va7b929i3TJm4kECM2HVxl-DDBRY")

# Загружаем расписание занятий из Excel-файла
schedule = pd.read_excel("https://docs.google.com/spreadsheets/d/10qauPwaMBwfLv9bzi13AxoHflszhexTK/edit?usp=sharing&ouid=113059829517749461289&rtpof=true&sd=true")

# Функция для обработки входящих сообщений
@bot.message_handler(commands=["raspi"])
def get_schedule(message):
    # Получаем номер группы из сообщения
    group_number = message.text.split(" ")[1]

    # Ищем расписание для указанной группы
    schedule_for_group = schedule[schedule["Группа"] == group_number]

    # Формируем ответ
    response = "Расписание занятий для группы {}:\n\n".format(group_number)
    for day in schedule_for_group["День"].unique():
        response += "{}:\n".format(day)
        for lesson in schedule_for_group[schedule_for_group["День"] == day].to_dict("records"):
            response += "    * {} ({}-{})\n".format(
                lesson["Предмет"], lesson["Аудитория"], lesson["Преподаватель"]
            )

    # Отправляем ответ пользователю
    bot.send_message(message.chat.id, response)

# Запускаем бота
bot.polling()
