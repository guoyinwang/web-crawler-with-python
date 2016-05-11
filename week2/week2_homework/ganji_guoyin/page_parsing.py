from bs4 import BeautifulSoup
import time as tm
import requests
import pymongo
import random

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
page_info = ganji['page_info']

header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
          'Cookie' : 'PSTM=1441482208; BIDUPSID=8719A6A764021F9CB718C9161CC6CE28; BDUSS=ZtNUlMLXJ2dmlrQ3pxQS1TOXQySWpibGtIQW5qRk1uVmhjZjNtaVFWcmk1a05YQVFBQUFBJCQAAAAAAAAAAAEAAAAYWihAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOJZHFfiWRxXNG; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=1451_7477_19713_18240_19782_17948_19805_19900_19558_19807_19843_19901_19860_15342_11469_10632; BAIDUID=3A933A4E9FA92621ECEA7C85AD666360:FG=1',
          }
proxy_list = [
    'http://117.177.250.151:8081',
    'http://111.85.219.250:3129',
    'http://122.70.183.138:8118',
    ]
proxy_ip = random.choice(proxy_list) # 随机获取代理ip
proxies = {'http': proxy_ip}

def page_parsing(url, headers = header):
    # time.sleep(2)
    header['Referer'] = '{}'.format(url)
    wb_data = requests.get(url, headers = header)
    print(url)
    print(wb_data.status_code)
    if wb_data.status_code == 404:
        pass
    else:
        soup = BeautifulSoup(wb_data.text, 'lxml')
        if not soup.find('title-name'):
            pass
        name = soup.select('h1.title-name')[0].text
        category = soup.select('ul.det-infor > li > span > a')[0].text
        price = soup.select('li > i.f22.fc-orange.f-type')[0].text
        areas = soup.select('ul.det-infor > li:nth-of-type(3) > a')
        print(areas)
        area = list(map(lambda x : x.text, areas))
        time = soup.select('i.pr-5')[0].text.strip().split('\xa0')[0]

        data = {'name' : name,
                'price' : price,
                'category' : category,
                'area' : area,
                'time' : time,
                'url' : url}
        print(data)
        page_info.insert_one(data)
        tm.sleep(2)



if __name__ == '__main__':
    url = 'http://bj.ganji.com/jiaju/2067064824x.htm'
    page_parsing(url)
