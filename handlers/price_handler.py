import requests
from telegram import Update
from telegram.ext import ContextTypes

CMC_API_KEY = 'f94dc9ae-1d6a-421f-85d2-b6d454caa5c4'
CMC_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

def fetch_top_cryptos():
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': CMC_API_KEY}
    response = requests.get(CMC_URL, headers=headers)
    data = response.json()
    
    if data['status']['error_code'] == 0:
        cryptos = data['data'][:5]  # Get top 5 cryptocurrencies
        message = "Top Cryptocurrencies:\n"
        for crypto in cryptos:
            name = crypto['name']
            price = crypto['quote']['USD']['price']
            change_24h = crypto['quote']['USD']['percent_change_24h']
            message += f"{name}: ${price:.2f}, 24h Change: {change_24h:.2f}%\n"
        return message
    else:
        return "Failed to fetch data\n Please try again later"

def fetch_crypto_by_symbol(symbol):
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': CMC_API_KEY}
    response = requests.get(CMC_URL, headers=headers)
    data = response.json()
    
    if data['status']['error_code'] == 0:
        for crypto in data['data']:
            if crypto['symbol'].upper() == symbol.upper():
                name = crypto['name']
                price = crypto['quote']['USD']['price']
                change_24h = crypto['quote']['USD']['percent_change_24h']
                return f"{name} ({symbol.upper()}):\nPrice: ${price:.2f}\n24h Change: {change_24h:.2f}%"
        return f"Cryptocurrency with symbol '{symbol}' not found."
    else:
        return "Failed to fetch data\n Please try again later"

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        symbol = context.args[0]
        message = fetch_crypto_by_symbol(symbol)
    else:
        message = fetch_top_cryptos()
    
    await update.message.reply_text(message)