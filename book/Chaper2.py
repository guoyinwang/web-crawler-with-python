from bs4 import BeautifulSoup
import requests
import urllib

url = 'http://www.pythonscraping.com/pages/warandpeace.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')
nameList = soup.find_all('span', {'class' : 'green'})
for name in nameList:
    print(name.text)

print('nameList over')
greenList = soup.find_all(class_ = 'green')
for green in greenList:
    print(green)

print('==========green over===========')

url1 = 'http://www.pythonscraping.com/pages/page3.html'

wb_data1 = requests.get(url1)
soup1 = BeautifulSoup(wb_data1.text, 'lxml')
for child in soup1.find('table', {'id' : 'giftList'}).children:
    print(child)
