import requests

api = "8e045d7eee2747589a87940bf9de28f7"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-06-18&sortBy=publishedAt&apiKey=" \
      "8e045d7eee2747589a87940bf9de28f7"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
