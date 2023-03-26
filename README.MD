### Можем проверять, является ли команда вызвана админом/владельцем и т.д.
#
```python
bot = telegram.Bot(token=TOKEN)

# Get information about a user in the group
user_id = 123456789 # Replace with the user ID you want to check
chat_id = -123456789 # Replace with the group chat ID
chat_member = bot.get_chat_member(chat_id, user_id)

# Check if the user is an admin
if chat_member.status == 'administrator':
    print('User is an admin!')
else:
    print('User is not an admin.')
```
[status](https://docs.python-telegram-bot.org/en/stable/telegram.chatmember.html#telegram.ChatMember.OWNER)
The member’s status in the chat. Can be ADMINISTRATOR, OWNER, BANNED, LEFT, MEMBER or RESTRICTED.

