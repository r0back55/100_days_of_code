import requests
from twilio.rest import Client

# Define constants for stock and company information
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# API endpoints and keys for stock data and news
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = ""
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ""

# Twilio account credentials
TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""

# Parameters for the stock API request
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

# Make a request to the stock API
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = response.json()["Time Series (Daily)"]

# Extract the latest two days of stock data
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])
print(yesterday_closing_price)

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday['4. close'])
print(day_before_yesterday_closing_price)

# Calculate the difference in closing prices
difference = yesterday_closing_price - day_before_yesterday_closing_price

# Determine if the stock price went up or down
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Calculate the percentage difference in closing prices
percentage_differance = round(difference / day_before_yesterday_closing_price * 100)
print(f"{percentage_differance}%")

# If the percentage difference is greater than 5% (positive or negative), fetch news articles
if abs(percentage_differance) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "language": "en"
    }

    # Make a request to the news API
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()["articles"]

    # Get the top three news articles
    top_three_articles = news_data[:3]

    # Format the articles for the message body
    formatted_articles = [(f"{STOCK_NAME}: {up_down}{percentage_differance}% \n"
                           f"Headline: {article['title']}. \n"
                           f"Brief: {article['description']}") for article in top_three_articles]

    # Initialize the Twilio client
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    # Send the formatted articles as SMS messages
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+",
            to="+",
        )
