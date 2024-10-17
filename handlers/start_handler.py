from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(' Welcome to Co1nCraze!\n Use /cmds to get the command list\n Made with love by Deep!'
)