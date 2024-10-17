from telegram import Update
from telegram.ext import ContextTypes

async def cmds(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /cmds command by sending a list of available commands to the user.
    """
    commands_list = (
        "/start - Start interacting with the bot\n"
        "/news - Get the latest crypto news\n"
        "/price - Get the current/latest price of cryptocurrencies\n"
        "/cmds - List all available commands"
    )
    
    await update.message.reply_text(commands_list)