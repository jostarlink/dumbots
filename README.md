# Dumbots
A list of dumb bots for experimentation, hooked via telegram.

## List of Bots

1. **SynBot** : *meaning, synonyms, antonyms of words*
2. **TriviBot** : *conducts trivia in a group from various categories and keeps scores for participating users*
3. **LogBot** : *logs the messages in a group , users can categorize the logs .*

### Installing Dependencies

--The bots use `python-telegram-bot` wrapper to process the messages from telegram . Install `python-telegram-bot` wrapper from
[https://github.com/python-telegram-bot/python-telegram-bot/] . You can either use pip or build from the code .


###Setting up the API TOKEN
--After registering for a telegram bot , you will receive a *TOKEN* . Set it as an environmental variable in your `.bashrc` file and include it in the respective bot file.

### Running the project

For running the project , use the following example of LogBot.py
```bash
python LogBot.py
```
