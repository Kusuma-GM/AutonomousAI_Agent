import requests

# 🔹 Replace this with your valid API key from https://newsapi.org/
NEWS_API_KEY = "YOUR_NEWSAPI_KEY"

def fetch_ai_news():
    """Fetches the top 5 AI news headlines from NewsAPI."""
    try:
        url = f"https://newsapi.org/v2/top-headlines?category=technology&apiKey={NEWS_API_KEY}"
        response = requests.get(url)

        if response.status_code == 401:
            print("❌ API Error: Unauthorized (Check API Key)")
            return []
        elif response.status_code != 200:
            print(f"❌ API Error: {response.status_code}")
            return []

        data = response.json()
        if "articles" in data:
            headlines = [f"{i+1}. {article['title']}" for i, article in enumerate(data["articles"][:5])]
            return headlines

        return []
    except Exception as e:
        print(f"❌ Error fetching news: {e}")
        return []
