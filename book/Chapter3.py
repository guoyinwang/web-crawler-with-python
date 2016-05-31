from bs4 import BeautifulSoup
import requests
import re

url = 'http://en.wikipedia.org/wiki/Kevin_Bacon'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

for link in soup.find('div',{'id' : 'bodyContent'}).findAll('a', href = re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.get('href'))