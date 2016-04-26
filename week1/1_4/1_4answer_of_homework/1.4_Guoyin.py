from bs4 import BeautifulSoup
import requests
import time
import urllib

url = 'http://weheartit.com/inspirations/taylorswift'
header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36'}

path = '/Users/Guoyin/Documents/Course/web crawler/Plan-for-combating-master/week1/1_4/1_4answer_of_homework/pics/'

urls = ['http://weheartit.com/inspirations/taylorswift?scrolling=true&page={}&before=174517611'.format(i) for i in range(1,11)]

def get_page(url):
    datas =[]
    wb_data = requests.get(url, headers = header)
    # print(wb_data)
    soup = BeautifulSoup(wb_data.text, 'lxml')


    imgs = soup.select('div > div > a > img')
    for img in imgs:
        data = {'image': img.get('src')}
        datas.append(data)
    return datas

def download(datas):
    for data in datas:
        for image in data:
            localUrl = data[image]
            localName = path + localUrl.split('/')[-2] + localUrl.split('/')[-1]
            urllib.request.urlretrieve(localUrl, filename = localName)

for url in urls:
    datas = get_page(url)
    download(datas)
    time.sleep(2)
    print(datas)

