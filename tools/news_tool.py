import os
import requests
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()


@tool
def get_latest_news(place: str) -> str:
    """
    Get latest news for a city, country, or location using GNews.
    """

    api_key = os.getenv("GNEWS_API_KEY")

    if not api_key:
        return "GNEWS_API_KEY not found in .env"

    url = "https://gnews.io/api/v4/search"

    params = {
        "q": place,
        "lang": "en",
        "country": "in",
        "max": 5,
        "apikey": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return f"Error: {response.text}"

    data = response.json()

    articles = data.get("articles", [])

    if not articles:
        return f"No news found for {place}"

    news_list = []

    for i, article in enumerate(articles, start=1):
        title = article.get("title", "No title")
        source = article.get("source", {}).get("name", "Unknown")
        published = article.get("publishedAt", "")
        url = article.get("url", "")

        news_list.append(
            f"{i}. {title}\n"
            f"   Source: {source}\n"
            f"   Published: {published}\n"
            f"   URL: {url}\n"
        )

    return "\n".join(news_list)

#
# if __name__ == "__main__":
#     result = get_latest_news.invoke({"place": "London"})
#     print(result)