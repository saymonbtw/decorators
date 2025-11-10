from datetime import datetime
from calendar import month_name
import locale
import uuid

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
pattern = "%d-%m-%Y %H:%M"
TOKEN = "8440845902:AAHY1gI2TDSWwcrKw5mk2dhWQDZbICVNpUg"
month_names = list(month_name)

buttons = ["start", "generate link", "play"]


async def generate_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Ссылка получена {uuid.uuid4().hex}")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Получаем аргумент команды /start
    argument = context.args
    user_date = datetime.now()
    user_month = month_names[user_date.month]
    user = update.message.from_user.name
    answer = f"{user_date.day} {user_month} {user_date.year} года в {user_date.hour}ч {user_date.minute}мин"
    if argument:
        print(argument[0])
        await update.message.reply_text(f'Получен аргумент: {argument[0]}')
    else:
        await update.message.reply_text(f'Привет, {user}, как дела?\nВы запустили бота {answer}')


if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("generate_link", generate_link))
    app.run_polling()
