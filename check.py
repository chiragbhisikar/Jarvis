import requests


def getArticles():
    response = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&apiKey=812149e860b84f9fa21c4359f2934744"
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
