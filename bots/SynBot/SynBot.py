#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages

from telegram.ext import Updater
import logging
import os
from nltk.corpus import wordnet as wn
from lib.wn import *  

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

ERROR_STR = 'Only a meaningful WORD is accepted!'
DUMB_STR  = 'I am too dumb to answer that!'

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def reply(bot, update):
    # get word
    word = update.message.text
    print 'Message : ',word
    if ' ' not in word:
        synms = wn.synsets(word)
        if synms:
            reply_msg = synms[0].definition()
            print 'Reply : ',reply_msg
            bot.sendMessage(update.message.chat_id, text=reply_msg)
        else:
            bot.sendMessage(update.message.chat_id, text=ERROR_STR)
    else:
        words = word.split(' ')
        if len(words) == 2 and words[0].lower() == 'like':
            synonyms =  synonymsOf(synsets(words[1]))
            _synonyms = [y for y in synonyms if y != synonyms[0]]
            reply_msg = ', '.join(_synonyms)
            print 'Reply : ',reply_msg
            if reply_msg:
                bot.sendMessage(update.message.chat_id, text=reply_msg)
            else:
                bot.sendMessage(update.message.chat_id, text=DUMB_STR)
        else:
            bot.sendMessage(update.message.chat_id, text=ERROR_STR)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(os.environ['SYN_BOT_TOKEN'])

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", help)

    # on noncommand i.e message - echo the message on Telegram
    dp.addTelegramMessageHandler(reply)

    # log all errors
    dp.addErrorHandler(error)

    # Start the Bot
    updater.start_polling()

    print 'Bot Started!!\n'

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
