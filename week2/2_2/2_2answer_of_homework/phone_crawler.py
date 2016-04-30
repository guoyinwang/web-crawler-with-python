from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
phone58 = client['phone58']
url_list = phone58['url_list']
url_list.remove()


url = 'http://bj.58.com/shoujihao/'

def get_links(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    # infolist > div > ul > div:nth-child(2) > ul > li:nth-child(2) > a.t > strong
    # infolist > div > ul > div.boxlist.boxbg > ul > li:nth-child(11) > a.t > strong
    nums = soup.select('strong.number')
    links = soup.select('a.t')

    for num, link in zip(nums, links):
        item_link = link.get('href')
        if item_link.split('//')[1].startswith('jump'):
            continue
        item_num = num.text
        data = {'link' : item_link,
                'num' : item_num}
        print(data)
        url_list.insert_one(data)

get_links(url)


