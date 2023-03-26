import telegram
from telegram.ext import Updater, CommandHandler
from decouple import config
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Replace YOUR_BOT_TOKEN with your bot's token
bot = telegram.Bot(config('token'))

# Define a dictionary to store the points for each participant
points = {}

# Define a function to handle the /addpoints command
def add_points(update, context):
    user_id = update.message.from_user.id
    chat_id = update.message.chat.id
    # chat_member = bot.get_chat_member(chat_id, user_id)

    chat_info = bot.get_chat(chat_id)
    is_admin = (chat_info.get_member(user_id).status in ['creator', 'administrator'])

    if is_admin:
        # Get the user to add points to
        user = context.args[0]

        # Get the number of points to add
        amount = int(context.args[1])
        # Add the points to the user's total
        if user in points:
            points[user] += amount
        else:
            points[user] = amount
        # Send a confirmation message
        update.message.reply_text(f"{user} now has {points[user]} points.")
    else:
        update.message.reply_text(f"You are not an administrator")


# Define a function to handle errors
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# Define a function to handle the /subtractpoints command
def subtract_points(update, context):
    user_id = update.message.from_user.id
    chat_id = update.message.chat.id
    # chat_member = bot.get_chat_member(chat_id, user_id)

    chat_info = bot.get_chat(chat_id)
    is_admin = (chat_info.get_member(user_id).status in ['creator', 'administrator'])

    if is_admin:
        # Get the user to subtract points from
        user = context.args[0]
        # Get the number of points to subtract
        amount = int(context.args[1])
        if int(amount):
        # Subtract the points from the user's total
            if user in points:
                points[user] -= amount
                if points[user] < 0:
                    points[user] = 0
                # Send a confirmation message
                update.message.reply_text(f"{user} now has {points[user]} points.")
            else:
                # Send an error message if the user doesn't have any points yet
                update.message.reply_text(f"{user} doesn't have any points yet.")
        else:
            update.message.reply_text(f"points have to be a number")
    else:
        update.message.reply_text(f"You are not an administrator")


# Create an Updater object and attach the command handlers
updater = Updater(config('token'), use_context=True)
updater.dispatcher.add_handler(CommandHandler('addpoints', add_points))
updater.dispatcher.add_handler(CommandHandler('subtractpoints', subtract_points))
# Add an error handler
updater.dispatcher.add_error_handler(error)

# Start the bot
updater.start_polling()
updater.idle()
