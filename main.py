import requests
from send_email import send_email

api = "8e045d7eee2747589a87940bf9de28f7"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-06-18&sortBy=publishedAt&apiKey=" \
      "8e045d7eee2747589a87940bf9de28f7"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)