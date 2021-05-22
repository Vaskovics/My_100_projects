import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MY_KEY = "I36D8EV8M8RESQ9E"
STOCK_API = "https://www.alphavantage.co/query"
NEWS_API_KEY = "3ef29d56305e4cd58f426c67b950aec7"
NEWS_API = "https://newsapi.org/v2/everything"
TWILIO_SID = "Ca1uTsxo5kcPvHNMF8T9YuLq38hq75O97scxGqjK"
TWILIO_AUTH_TOKEN = "ec2cfff303adaa545a4f31a56ffa6610"

stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API
}
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(STOCK_API, params=stock_param)
response.raise_for_status()
data = response.json()

# Defined today adn yesterday
now = datetime.today()
today = now.date()
yesterday = today - timedelta(days=1)
day_before_yesterday = yesterday - timedelta(days=1)

# Yesterday and day before yesterday
yesterday_close = data["Time Series (Daily)"][str(yesterday)]["4. close"]
day_before_yest_close = data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"]
print(yesterday_close)
print(day_before_yest_close)

difference = float(yesterday_close) - float(day_before_yest_close)
up_down = None
if difference > 0:
    up_down = "🔻"
else:
    up_down = "ᐃ"

diff_percent = round((difference / float(yesterday_close)) * 100)


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

if abs(diff_percent) > 1:
    news_param = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,

    }
    response_news = requests.get(NEWS_API, params=news_param)
    articles = response_news.json()["articles"]
    print(articles)
    tree_articles = articles[0:3]

# 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
formatted_articles = [
    f"{STOCK}: {up_down}{diff_percent}% Headline: {article['title']}. \nBrief: {article['description']}" for article in
    tree_articles]
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="+13519998463",
        to="+4472427254",
    )
