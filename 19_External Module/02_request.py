
import requests

r = requests.get('https://api.github.com/events')

# print(r.text)

with open("Gauttam.txt","w") as f:
    f.write(r.text)

