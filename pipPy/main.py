from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *


updater = Updater('5153530856:AAFo2poFM33Hkt6xvp6rQOUXVNbSZ9KPSg0')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('game', candy_join))
updater.dispatcher.add_handler(CommandHandler('start_game', start_game))

print('server start')
updater.start_polling()
updater.idle()