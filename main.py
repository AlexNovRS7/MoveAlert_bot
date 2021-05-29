from pyrogram import Client, filters
import time
import itertools


excercises = ["first", "second", "third"]

app = Client(
    "MoveAlert_bot",
    bot_token="1769571098:AAFvDWOnyMqYdL8UwLia-XbYQT0uOFLJkMc"
)

@app.on_message(filters.text & filters.private)
def my_handler(client, message):
    if message.text == '/start':
        message.reply_text("Hello, I will remind you to move while your are working.")
        message.reply_text("I am based on this Athlean-X's video: https://youtu.be/h3PZZyoXnKU")
    
    if message.text == '/sitting':
        time.sleep(60*30)
        while message.text != '/finish':
            for excercise in itertools.cycle(excercises):
                message.reply_text(excercise)
                time.sleep(60*30)

    if message.text == '/snooze':
        message.reply_text("This button don't work yet")

    if message.text == '/done':
        message.reply_text("This button don't work yet")

app.run()