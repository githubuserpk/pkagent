import requests
import nltk

from nltk.sentiment import SentimentIntensityAnalyzer

def fetch_news(query, api_key):
    url = f'https://newsapi.org/v2/top-headlines?q={query}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return [article['content'] for article in articles if article['content']]
    else:
        print(f"Error fetching news: {response.status_code}")
        return []

def analyze_sentiment(text):
    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment = sentiment_analyzer.polarity_scores(text)['compound']
    if sentiment > 0.2:
        return 1  # Positive
    elif sentiment < -0.2:
        return -1  # Negative
    else:
        return 0  # Neutral
    

# Download the VADER lexicon
nltk.download('vader_lexicon')


def main():
    company = "Google"
    api_key = "8bed1e3fc5914c54ba04a57224fbcc29"  # Replace with your News API key
    news_articles = fetch_news(company, api_key)
    for article in news_articles:
        sentiment = analyze_sentiment(article)
        print(f"Sentiment: {sentiment}, Article: {article[:100]}...")

if __name__ == "__main__":
    main()

