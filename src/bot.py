from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler
from telegram.ext import filters
import asyncio
from handlers import start_command, lyrics_command, handle_message
from callbacks import callback_handler
from config import *


if __name__=="__main__":
	app=Application.builder().token(TELEGRAM_BOT_TOKEN).build()
	app.add_handler(CommandHandler("start", start_command))
	app.add_handler(CommandHandler("lyrics", lyrics_command))
	app.add_handler(MessageHandler(filters.TEXT, handle_message))
	app.add_handler(CallbackQueryHandler(callback_handler))
	
	
	print("🔄 Initializing bot...")
	print(f"✅ Bot started successfully!")
	print(f"📡 Listening for messages...")

	app.run_polling(poll_interval=2)