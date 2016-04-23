#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages

from telegram.ext import Updater
from telegram import ReplyKeyboardMarkup
import logging
import os
#from lib.wn import *  
import hickle as hkl
from random import randint

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

zero, one, two, three, four, five = ('0','1','2','3','4','5')
reply_markup = ReplyKeyboardMarkup([[zero, one, two], [three, four, five]], one_time_keyboard=True)

S,E,Q,K,M = ('start', 'end','stale','kid','meme')
qnum = -1
score = {}
unames = []
state = Q

# load trivia
trivia = hkl.load('data/tech.hkl')

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def reply(bot, update):
    global qnum
    global trivia
    global score
    global unames
    global state
    _score = 0

    # get message
    message = update.message.text
    uname = update.message.from_user.username
    fname = update.message.from_user.first_name
    print 'Message : ',message
    print 'from : ',fname
    reply_msg = 'Something went wrong!'

    if uname not in unames:
        unames.append(uname)
        score[uname] = 0

    if message == S:
        # start the trivia session
        state = S
    elif message == E:
        state = E

    if state != Q:
        # send ques + choices here
        if state == S:
            #  Get Question
            qnum = randint(0,len(trivia))
            reply_msg = trivia[qnum]['ques'] + '\n' + trivia[qnum]['choices']
            bot.sendMessage(update.message.chat_id, text=reply_msg,reply_markup=reply_markup)
            state = K
            #old_qnum = qnum

        if message in ['0','1','2','3','4','5'] and state != S:
            if trivia[qnum]['ansnum'] == int(message):
                reply_msg = 'Correct ' + fname + '! ' + trivia[qnum]['ans'] + '.'
                _score = 10
            else:
                reply_msg = 'Wrong ' + fname + '! ' + trivia[qnum]['ans'] + '.'
                _score = -5

            for u in unames:
                if u == uname:
                    score[u] += _score
                reply_msg += u + ' : ' + str(score[u]) + '\n'
            #reply_msg += ', '.join(unames)

            bot.sendMessage(update.message.chat_id, text=reply_msg)

            # next question
            qnum = randint(0,len(trivia))
            reply_msg = trivia[qnum]['ques'] + '\n' + trivia[qnum]['choices']
            bot.sendMessage(update.message.chat_id, text=reply_msg,reply_markup=reply_markup)
        

'''
    if word == Means or word == Syno or word == Anto or word == Eg:
        print 'Selected', word
        if word == Means:
            reply_msg = synsets(gWord)[0].definition()
        elif word == Syno:
            reply_msg = ', '.join(synonymsOf(synsets(gWord)))
        elif word == Anto:
            reply_msg = ', '.join(antonymsOf(synsets(gWord)))
        else:
            reply_msg = '\n'.join(wordEg(synsets(gWord)))

        if reply_msg:
            print 'Reply : ', reply_msg
            bot.sendMessage(update.message.chat_id, text=reply_msg)
        else:
            print 'Reply : Something went wrong!'
            bot.sendMessage(update.message.chat_id, text='Something went wrong!')
    else:
        gWord = word
        reply_markup = ReplyKeyboardMarkup([[one, two, three, four]], one_time_keyboard=True)
        bot.sendMessage(update.message.chat_id, text="What do you want?",reply_markup=reply_markup)
'''


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():

    # Create the EventHandler and pass it your bot's token.
    updater = Updater(os.environ['TRIVIA_BOT_TOKEN'])

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
