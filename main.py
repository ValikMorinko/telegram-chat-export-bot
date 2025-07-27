
import logging
import json
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


TOKEN = "8380860231:AAEQWAITYuI3aEvOBIzAh8I_nvaP5-lGBT8"


# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# Файл для хранения ролей
ROLES_FILE = "roles.json"


# Функция для загрузки ролей
def load_roles():
    if not os.path.exists(ROLES_FILE):
        return {"admins": []}
    with open(ROLES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    
    
# Функция сохранения ролей
def save_roles():
    with open(ROLES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Бот запущен и готов к работе!")
    
    
# Команда /stop
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⛔ Бот остановлен!")
    
    
# Команда /status
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    roles = load_roles()
    admins = roles.get("admins", [])
    if admins:
        text = "✅ Бот работает\n👑 Администраторы:\n" + "\n".join(admins)
    else:
        text = "✅ Бот работает\nАдминистраторов пока нет."
    await update.message.reply_text(text)

    
    
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(CommandHandler("status", status))
    
    
    
    print("✅ Бот запущен...")
    app.run_polling()
    
    
if __name__ == "__main__":
  main()
    



