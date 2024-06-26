
# Tbilisi Transport Company Bot

This Telegram bot provides real-time information about buses at stops in Tbilisi, Georgia, using the API of the Tbilisi Transport Company. Users can message a stop's code, and the bot will return the buses available at that stop along with their arrival times.

## Requirements

- Python 3.x
- `python-telegram-bot` library
- `requests` library

## Installation

1. Clone or download this repository.
2. Install the required libraries by running:
   ```
   pip install python-telegram-bot requests
   ```
3. Obtain a Telegram bot token from the [BotFather](https://t.me/BotFather) on Telegram.
4. Insert your bot token into the `ttc_bot.py` file's "bot_token".

## Usage

1. Start the bot by running:
   ```
   python ttc_bot.py
   ```
2. Open Telegram and start a conversation with your bot.
3. Input the stop's code when prompted.
4. The bot will reply with the available buses at the specified stop and their arrival times.

## Commands

- `/start` - Start the bot and get instructions.

## Acknowledgments

This bot utilizes the API of the Tbilisi Transport Company to provide real-time bus information.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is the property of Framework LLC and is licensed under the Framework License.

---

Feel free to customize it according to your project's needs!
