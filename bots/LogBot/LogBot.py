#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages

from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import ReplyKeyboardMarkup
import logging
import os

gWord = 'internet'

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)
rmessage = {}
category = ""
status = ""
filenameus=""
counter = 0
# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def reply(bot, update):
    global gWord
    global message
    global category
    global status
    global filenameus
    # get message line
    line = update.message.text

    linelist = line.split(" ")
    if status == "started" and linelist[0] != "@loggedbot":
        uname = update.message.from_user.username
        mdate = update.message.date
        rmessage["uname"] = uname
        rmessage["date"] = mdate
        rmessage["message"] = line
        print rmessage
        directory = update.message.chat.title
        if not os.path.exists(directory):
            os.makedirs(directory)
        file = open("./"+directory+"/"+category+".txt",'a')

        file.write("[ "+str(rmessage["date"])+" ]"+str(rmessage["uname"])+" : "+rmessage["message"])
        file.write("\n")
        file.close()

    elif linelist[0] == "@loggedbot" and linelist[1] != "end" and status != "started":
        filenameus = ""
        for l in linelist[1:len(linelist)]:
            filenameus += l+"_"

        n=len(filenameus)
        filenameus=filenameus[:-1]
        category = filenameus
        directory = update.message.chat.title
        if not os.path.exists(directory):
            os.makedirs(directory)
        file = open("./"+directory+"/"+category+".txt",'a')
        titletime = str(update.message.date)
        file.write("\n"+"----------"+titletime+"----------- \n")
        file.close()
        reply_msg = " I will start the log of "+category+" discussion for group "+str(update.message.chat.title)
        bot.sendMessage(update.message.chat_id, text=reply_msg)

        status = "started"

    elif linelist[0] == "@loggedbot" and linelist[1] == "end" and status == "started":
        status = "ended"

    elif linelist[0] == "@loggedbot" and linelist[1] == "end" and status == "ended":
        print "No discussion to end"

    else:
        uname = update.message.from_user.username
        mdate = update.message.date
        rmessage["uname"] = uname
        rmessage["date"] = mdate
        rmessage["message"] = line
        print rmessage
        directory = update.message.chat.title
        if not os.path.exists(directory):
            os.makedirs(directory)
        file = open("./"+directory+"/general.txt",'a')

        file.write("[ "+str(rmessage["date"])+" ]"+str(rmessage["uname"])+" : "+rmessage["message"])
        file.write("\n")
        file.close()







def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and passs it your bot's token.
    updater = Updater(os.environ['LOGBOT'])

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addHandler(CommandHandler("start", start))
    dp.addHandler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.addHandler(MessageHandler([Filters.text],reply))

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
