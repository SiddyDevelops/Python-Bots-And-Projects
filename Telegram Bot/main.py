import logging
from telegram.ext import * 
import responses

API_KEY = '*****************************************' 

# Set Up the logging 
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s %(message)s", level=logging.INFO)
logging.info('Starting Bot...')

def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot developed by Siddharth Singh. What\'s up?')

def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')

def custom_command(update, context):
    update.message.reply_text('This is an custom command, you can add whatever text you want here.')

def handle_message(update, context):
    text =  str(update.message.text).lower()
    response = responses.get_response(text)
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    update.message.reply_text(response)

def error(update, context):
    logging.error(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    updater = Updater(API_KEY,use_context=True)
    dp = updater.dispatcher

    # Commands 
    dp.add_handler(CommandHandler('start', start_command))            
    dp.add_handler(CommandHandler('help', help_command))            
    dp.add_handler(CommandHandler('custom', custom_command))    

    # Messages 
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()        