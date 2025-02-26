from telegram import InlineKeyboardMarkup
import lyricsgenius
import json
from utils.parser_4096 import parser_4096
from config import genius

async def callback_handler(update, context):
	await update.callback_query.answer()
	song_id=update.callback_query.data
	song_result=genius.search_song(song_id=song_id)			#Song object data here is found as Song object (.to_json() converts it to a string, then json.loads() converts it to json/dict)
	
	if type(song_result) is lyricsgenius.types.song.Song:
		# print("Inside callback: type of song_result: ", type(song_result))
		lyrics_string_container=json.loads(song_result.to_json())				#.to_json() converts Song object to string,   json.loads() converts string dictionary to dictionary
		lyrics_string=lyrics_string_container["lyrics"]
		song_full_title= "**" + lyrics_string_container["full_title"] + "**"
		final_string= song_full_title + "\n\n" + lyrics_string + "\n\nSupport us by sharing the bot!"
		list_of_4096_characters=parser_4096(final_string)
		for block in list_of_4096_characters:
			await update.callback_query.message.reply_text(block)
		if update.callback_query.message:
			await update.callback_query.delete_message()
	else:
		await update.callback_query.edit_message_text("No lyrics data available.")
		await update.callback_query.edit_message_reply_markup(InlineKeyboardMarkup([[]]))