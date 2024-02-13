import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
}

scripts_url = "https://seinfeldscripts.com/seinfeld-scripts.html"

req = requests.get(scripts_url, headers=headers)
print(req.text)

soup = BeautifulSoup(req.text, "html.parser")
print(soup.prettify())
