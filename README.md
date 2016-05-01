![](https://telegram.org/img/t_logo.png)

# Dumbots
 This repository is a collection of dumb bots (*bots that are neither generative nor rule-based*). We are using Telegram's bot API for testing our chatbots, because we are familiar with it. Check out the ./bots folder. 

## List of Bots

1. **SynBot** : *meaning, synonyms, antonyms of words*
2. **TriviBot** : *conducts trivia in a group from various categories and keeps scores for participating users*
3. **LogBot** : *logs the messages in a group , users can categorize the logs .*

## Installing Dependencies

![](https://raw.githubusercontent.com/python-telegram-bot/logos/master/logo-text/png/ptb-logo-text_768.png)

The bots use **python-telegram-bot** wrapper to process the messages from telegram . **python-telegram-bot** wrapper from [here](https://github.com/python-telegram-bot/python-telegram-bot/) . You can either use pip or build from the source.

## Setting up the API TOKEN

![](http://botsfortelegram.com/media/bot-father.png)

Talk to the BotFather for creating your own bot. It is pretty simple. After registering for a telegram bot , you will receive a *TOKEN* . Set it as an environmental variable in your `.bashrc` file and include it in the respective bot file.

## Running the project

For running the project , use the following example of LogBot.py
```bash
python LogBot.py
```

## Issues

Facing problems? Need more features? Welcome to Issues. Bitch bout it [here](https://github.com/ChatAI/dumbots/issues). 

## Licence : GPL v3

The GPL is a copyleft license, which means that derived works can only be distributed under the same license terms. [http://www.gnu.org/licenses/gpl-3.0.en.html](More).
