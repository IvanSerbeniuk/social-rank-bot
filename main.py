import telegram
from telegram.ext import Updater, CommandHandler
import logging
from decouple import config

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Create a new bot instance
bot = telegram.Bot(config('token'))

points = {}

# Define a command that adds points to a participant
def add_points(update, context):
    # Check if the user is the group owner
    if update.message.from_user.id == update.message.chat.owner.id:
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
        # Send an error message if the user is not the group owner
        update.message.reply_text("Only the group owner can add points.")



# Define a command that subtracts points from a participant
def subtract_points(update, context):
    # Check if the user is the group owner
    if update.message.from_user.id == update.message.chat.owner.id:
        # Get the user to subtract points from
        user = context.args[0]
        # Get the number of points to subtract
        amount = int(context.args[1])
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
        # Send an error message if the user is not the group owner
        update.message.reply_text("Only the group owner can subtract points.")



# Define a function to handle errors
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)



# Define a function that sets up the bot and starts polling for new messages
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add handlers for the add_points and subtract_points commands
    dp.add_handler(CommandHandler('addpoints', add_points))
    dp.add_handler(CommandHandler('subtractpoints', subtract_points))

    # Add an error handler
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
