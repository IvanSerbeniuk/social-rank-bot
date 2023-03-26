import telegram
from telegram.ext import Updater, CommandHandler
from decouple import config

# Replace YOUR_BOT_TOKEN with your bot's token
bot = telegram.Bot(config('token'))

# Define a dictionary to store the points for each participant
points = {}

# Define a function to handle the /addpoints command
def add_points(update, context):
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


# Define a function to handle the /subtractpoints command
def subtract_points(update, context):
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


# Create an Updater object and attach the command handlers
updater = Updater(token='5724159742:AAFtIdXqoBKi0yHFbBbq443FT9DXJQsF6yU', use_context=True)
updater.dispatcher.add_handler(CommandHandler('addpoints', add_points))
updater.dispatcher.add_handler(CommandHandler('subtractpoints', subtract_points))

# Start the bot
updater.start_polling()
updater.idle()
