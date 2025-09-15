import requests # pip install requests

query = input("What type of news are you interested in today? ")
api = "319f94225c5148c3a94a42841c25b720"
# url = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-01&sortBy=publishedAt&apiKey={api}"
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-01&sortBy=publishedAt&apiKey={api}"
print(url)
r =  requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")
