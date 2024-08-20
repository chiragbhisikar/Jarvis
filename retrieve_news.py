from apiKey import api_key
import requests


def getArticles():
    response = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    )

    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()

        # Extract the headlines
        articles = data.get("articles", [])

        # for article in articles:
        #     print(article["title"])

        return articles
    else:
        print(f"Failed to retrieve data: {response.status_code}")
