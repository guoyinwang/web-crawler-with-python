import requests
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl,level = 0):
    global pages
    if level >= 3:
        return
    baseUrl = "http://en.wikipedia.org"
    wb_data = requests.get(baseUrl + pageUrl)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    for link in soup.find_all('a', href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.get('href') not in pages:
                pages.add(link.get('href'))
                print(link.get('href'))
                getLinks(link.get('href'), level + 1)


getLinks("")