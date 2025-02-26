# Lyrics Genius Telegram Bot

A Telegram bot that fetches song lyrics using the Genius API.

## Features
- Search for song lyrics by track or artist.
- Select from the top results via inline buttons.
- Displays full lyrics, split if needed.

## Installation
1. **Clone the repository**  
   ```bash
   git clone https://github.com/yonaseth12/lyrics-provider-tg-bot.git
   cd LyricsFromTG_Bot
   ```

## 2. Install Dependencies

Before running the bot, you need to install the required dependencies. In your project directory, run:

```bash
pip install -r requirements.txt
```

## 3. Set API Tokens in `config.py`

In the `config.py` file, set your API tokens as follows:

```python
# config.py
TELEGRAM_BOT_TOKEN = "your-telegram-bot-token"
TOKEN_GENIUS = "your-genius-api-token"
BOT_USERNAME = 'your-telegram-bot-username"
```

## 4. Run the Bot

Run the following command to start the bot:

```bash
python src/bot.py
```

## 5. Commands

Once the bot is running, you can interact with it using the following commands:

- `/start` - Welcome message
- `/lyrics` - Search for lyrics

## 6. Built With

This project is built using the following technologies:

- **Python**
- **python-telegram-bot**
- **Genius API**
