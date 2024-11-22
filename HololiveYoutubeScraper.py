import requests
from bs4 import BeautifulSoup

import UrlList

talent_to_url = UrlList.get_talents()

def is_live():
    for i in talent_to_url:
        response = requests.get(i['Url'])
        if "Tap to watch live" in response.text:
            print(i['Name'] + " Is live")

# for url in talent_to_url:
#     print(url['Url'])
is_live()