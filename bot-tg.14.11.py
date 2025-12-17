from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Привет 👋", "Помощь ❓"], ["Весёлое сообщение 😄", "Прощай 👋", "Числа"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Привет! Я бот с кнопками. Выбери действие:", reply_markup=reply_markup
    )

async def numbers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Введи два числа, разделённые пробелом:")
    context.user_data['waiting_for_numbers'] = True

async def handle_numbers_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get('waiting_for_numbers'):
        return

    text = update.message.text
    list1 = text.split()
    list2 = []

    for element in list1:
        if element.isdigit():
            list2.append(int(element))
        else:
            await update.message.reply_text("Обнаружен текст! Выход.")
            context.user_data['waiting_for_numbers'] = False
            return

    if len(list2) != 2:
        await update.message.reply_text("Введи ровно два числа. Выход.")
        context.user_data['waiting_for_numbers'] = False
        return

    otvet = list2[0] + list2[1]
    await update.message.reply_text(f"Ответ: {otvet}")
    context.user_data['waiting_for_numbers'] = False

# Ответ на текстовые сообщения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # Проверяем, ждём ли мы ввод чисел
    if context.user_data.get('waiting_for_numbers'):
        await handle_numbers_input(update, context)
        return

    match text:
        case "привет" | "привет 👋":
            await update.message.reply_text("Привет! Рад тебя видеть 😎")
        case "помощь" | "помощь ❓":
            await update.message.reply_text("Вот что я умею:\n- Привет 👋\n- Весёлое сообщение 😄\n- Прощай 👋\n- Числа")
        case "весёлое" | "веселое" | "весёлое сообщение 😄":
            await update.message.reply_text(
                "😆 Вот тебе шутка: Почему программисты любят кофе? Потому что без него код не компилируется!")
        case "прощай" | "пока" | "прощай 👋":
            await update.message.reply_text("Пока! 👋 До скорой встречи!")
        case "числа":
            await numbers(update, context)
        case _:
            await update.message.reply_text("Я пока не понимаю это сообщение 🤔")

# Основная функция запуска бота
def main():
    load_dotenv()
    TOKEN = os.getenv("TOKEN")

    app = ApplicationBuilder().token(TOKEN).build()

    # Обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()