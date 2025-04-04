import requests
import os

def fetch_ai_news():
    api_key = "ef2f76a804ed4fb8bf299e40fffba6b9"  # ✅ Your API key
    url = f"https://newsapi.org/v2/everything?q=artificial+intelligence&sortBy=publishedAt&pageSize=5&apiKey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"❌ API Error: {data.get('message', 'Unknown error')} ({response.status_code})")
            return []

        articles = data.get('articles', [])
        headlines = [
            f"{idx + 1}. {article['title']} - {article['source']['name']}"
            for idx, article in enumerate(articles)
            if 'title' in article and 'source' in article
        ]

        # Save headlines to a file
        os.makedirs("output", exist_ok=True)
        with open("output/web_data.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(headlines))

        print("✅ News saved to 'output/web_data.txt'")
        for headline in headlines:
            print(f"> {headline}")

        return headlines

    except Exception as e:
        print(f"❌ Error fetching news: {e}")
        return []
