from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Zdarova {update.effective_user.first_name}!')

list_gamers = []

def start_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text('Этот бот еще находится на этапе разработки. Список команд с описанием можно посмотреть по команде /help')       

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi - приветствует по имени\n/time - показывает текущее время\n/help - показывает список команд с описанием \n/sum - считает сумму из двух чисел, написать нужно через пробел (например /sum 25 76)')
    
def time_command(update: Update, context: CallbackContext):
    log(update, context)
    current_time = datetime.datetime.now().time()
    update.message.reply_text(f'{current_time.hour} часов {current_time.minute} минут и {current_time.second} секунд')


def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()  #/sum 41234 1234123
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')

def candy_join(update: Update, context: CallbackContext):
    global list_gamers
    current_user = update.effective_user.id
    if current_user not in list_gamers:
        list_gamers.append(current_user)
        log(update, context)
        context.bot.send_message(current_user, 'Теперь Вы в игре')
        for user_id in list_gamers:
            context.bot.send_message(user_id, f'всего {len(list_gamers)} игроков')

def start_game(update: Update, context: CallbackContext):
    current_user = update.effective_user.id
    if current_user == list_gamers[0]:
        for user_id in list_gamers:
            context.bot.send_message(user_id, f'Игра началась\nВсего 100 конфет. Каждый игрок по очереди берет не более 10 конфет.\n Ходит игрок по имени')

current_time = datetime.datetime.now().time()
