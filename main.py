from telegram.ext import ApplicationBuilder, CommandHandler



#IMPORT DIFFERENT HANDLERS BASED ON TYPE OF FUNCTIONALITY
from handlers.start_handler import start  # Import the start handler
from handlers.command_handler import cmds
from handlers.news_handler import news
from handlers.price_handler import price
# Define your Telegram bot token
TELEGRAM_TOKEN = '7554746830:AAEjDjpKG11t6KStufdr1K6FL4dxSEkX0Mc'

def main():
    # Initialize the bot application
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # START
    application.add_handler(CommandHandler("start", start))
    # LIST OF COMMANDS
    application.add_handler(CommandHandler("cmds", cmds))
    #NEWS
    application.add_handler(CommandHandler("news", news))
    #PRICE
    application.add_handler(CommandHandler("price", price))
    
    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    
    main()
    
    
    
 