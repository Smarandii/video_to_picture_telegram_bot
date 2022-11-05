# multitool

## Telegram bot for content making automation:
- converts text from [@economika](https://t.me/economika) to picture with signature and post with hashtags

## Usage:
- send text for picture signature
- forward post from [@economika](https://t.me/economika) telegram channel
- you also can add text signature in forward message comment

## Run this bot localy on your computer:
1. run **cmd**
1. change working directory to repository directory (`cd` command)

**Pro-tip: To change drive in Windows use (D: - change drive to drive D | C: - change drive to drive C)**
1. run `python -m venv env` with **cmd** in repository directory
1. run virtual environment "env" (`.\env\Scripts\activate` for Windows)
1. run `pip install -r requirements.txt`
2. [get telegram bot token](t.me/BotFather)
3. add token in `bot.py` in `token` variable
4. run `python bot.py`
5. go to your bot (BotFather gave you link to your bot at step 2) and send /start
