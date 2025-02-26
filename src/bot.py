from telegram.ext import Application, CommandHandler
import lyricsgenius
from config import *



active_status=False		#Used to track whether user is inserting other input or lyrics search word

genius=lyricsgenius.Genius(access_token=TOKEN_GENIUS, response_format="plain", timeout=12)

async def start_command(update, context):
	await update.message.reply_text("Use /lyrics to search for lyrics.")

async def lyrics_command(update, context):
	await update.message.reply_text("Search by track/artist: ")
	global active_status
	active_status=True

if __name__=="__main__":
	app=Application.builder().token(TELEGRAM_BOT_TOKEN).build()
	app.add_handler(CommandHandler("start", start_command))
	app.add_handler(CommandHandler("lyrics", lyrics_command))
	
	app.run_polling(poll_interval=2)
