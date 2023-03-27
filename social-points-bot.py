import telegram
from telegram.ext import Updater, CommandHandler
from decouple import config
import logging


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

bot = telegram.Bot(config('token'))

# Gets user and chat id
def get_id_chat_user(update):
    user_id = update.message.from_user.id
    chat_id = update.message.chat.id
    return user_id, chat_id


# Define a dictionary to store the points for each participant
points = {}

def Admin_validation(user_id, chat_id):
    chat_info = bot.get_chat(chat_id)
    return chat_info.get_member(user_id).status in ['creator', 'administrator']

def Number_validation(numb, update):
    try:
        return int(numb)
    except:
        update.message.reply_text(f"points have to be a number")
        return 0

def Update_points(user, update, amount):
    if user in points:
        points[user] += amount
    else:
        points[user] = amount
    update.message.reply_text(f"{user} now has {points[user]} points.")

# Define a function to handle the /addpoints command
def add_points(update, context):
    user_id, chat_id = get_id_chat_user(update)

    is_admin = Admin_validation(user_id, chat_id)

    if not is_admin:
        update.message.reply_text("You are not an administrator")
        return
        
    user = context.args[0]
    amount = Number_validation(context.args[1], update)

    # Add the points to the user's total
    Update_points(user, update, amount)

    
# Define a function to handle the /subtractpoints command
def subtract_points(update, context):
    context.args[1] = '-' + context.args[1]
    add_points(update, context)


# Define a function to handle errors
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# Create an Updater object and attach the command handlers
updater = Updater(config('token'), use_context=True)
updater.dispatcher.add_handler(CommandHandler('addpoints', add_points))
updater.dispatcher.add_handler(CommandHandler('subtractpoints', subtract_points))
# Add an error handler
updater.dispatcher.add_error_handler(error)

# Start the bot
updater.start_polling()
updater.idle()