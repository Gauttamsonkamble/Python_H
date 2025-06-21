
import requests  # pip install request


query = input("What types of news are you interested in today? ")

api = "use your key"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-16&sortBy=publishedAt&apiKey={api}"

print(url)

r = requests.get(url)

data = r.json()

articles = data["articles"]

for index,article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    # print(article["url"])
    print("\n ********************************************************* \n")

