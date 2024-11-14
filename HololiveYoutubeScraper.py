import requests
from bs4 import BeautifulSoup

from UrlList import get_urls

urls = [get_urls()[1]]
for url in urls:
    response = requests.get(url)
    if "Tap to watch live" in response.text:
        print("Is live")
    else:
        print("Not live")

