import logging

from telegram.ext import Updater, CommandHandler 

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s -%(name)s - %(levelname)s - %(message)s'
)


updater = Updater(token='1212730002:AAGGB2DvMOER1qe7A73NqOVT7mbGvMFb5JY')
dispatcher = updater.dispatcher

def start(upd, ctx):
	ctx.bot.send_message(
		chat_id=upd.effective_chat.id,
		text="Hello",
	)

    
start_handler = CommandHandler(
'start', start
)


dispatcher.add_handler(start_handler)

updater.start_polling()
