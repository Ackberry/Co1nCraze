import requests
from telegram import Update
from telegram.ext import ContextTypes

NEWS_API_KEY = '992808adac96405384d5f47135a46278'
NEWS_API_URL = f'https://newsapi.org/v2/everything?q=cryptocurrency&sortBy=publishedAt&apiKey={NEWS_API_KEY}'


def fetch_crypto_news():
    response = requests.get(NEWS_API_URL)
    data = response.json()
    if data['status'] == 'ok':
        articles = data['articles'][:5]
        news_message = ""
        for article in articles:
            title  = article['title']
            url = article['url']
            news_message += f"{title}\n Read more: {url}\n\n"
        return news_message
    else:
        return "Failed to fetch news. Please try again later"
    
    
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /news command by sending the latest crypto news to the user.
    """
    news_message = fetch_crypto_news()
    await update.message.reply_text(news_message)