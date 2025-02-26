from telegram.ext import Application, CommandHandler
from handlers import start_command, lyrics_command, handle_message
from config import *


if __name__=="__main__":
	app=Application.builder().token(TELEGRAM_BOT_TOKEN).build()
	app.add_handler(CommandHandler("start", start_command))
	app.add_handler(CommandHandler("lyrics", lyrics_command))
	
	app.run_polling(poll_interval=2)
