<!-- ## This code creates a Telegram bot that allows administrators to add and subtract points from members of a group chat.



The following libraries are imported: (Attach to each documentation)

- telegram.ext: This library provides tools to build bots for Telegram using Python.
- Upgrader: This class is used to create an Updater object that continuously checks for updates from Telegram and handles them.
- CommandHandler: This class is used to handle Telegram commands.
- decouple.config: This library is used to store sensitive data such as the bot token in a .env file.
After importing the necessary libraries, the bot's token is retrieved from the .env file and a Bot object is created. A dictionary called points is also created to store the points for each participant.<br><br>
    **Note**: Script has old library 'python-telegram-bot==13.12'. Doesn't work with latest version python-telegram-bot<=13.15<br>

The add_points and subtract_points functions are defined to handle the /addpoints and /subtractpoints commands, respectively. Both functions first check if the user sending the command is an administrator before performing the requested action. If the user is an administrator, the function gets the user to add/subtract points from and the number of points to add/subtract, and updates the points dictionary accordingly. A confirmation message is then sent to the chat. If the user is not an administrator, an error message is sent.

An error handler function is also defined to handle any errors that occur while the bot is running.

Finally, an Updater object is created and the command handlers are attached to it. The bot is started using the start_polling() method and runs indefinitely until interrupted by the user.
 -->


# Points Bot
A simple Telegram bot that keeps track of points for different users in a chat.

## Dependencies
python-decouple<br>
python-telegram-bot


## Usage
To use the bot, create a Telegram bot using the BotFather and obtain an API token.<br>

Set the API token in a .env file in the same directory as the script using the following format:
> token=(bot_token)

To run the bot, simply execute the script:
> python points_bot.py
## Commands
- /addpoints <user> <points>: Adds points to the specified user's total. Only admins can use this command.
- /subtractpoints <user> <points>: Subtracts points from the specified user's total. Only admins can use this command.


