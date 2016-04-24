from bs4 import BeautifulSoup
import requests
import time

url = 'http://weheartit.com/inspirations/taylorswift'
header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36'}
# proxies = {"http": "http://121.69.29.162:8118"}

urls = ['http://weheartit.com/inspirations/taylorswift?scrolling=true&page={}&before=174517611'.format(i) for i in range(1,10)]

def get_page(url):
    datas =[]
    wb_data = requests.get(url, headers = header)
    # print(wb_data)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # main-container > div > div.grid-thumb.grid-responsive > div:nth-child(56)
    # main-container > div > div.grid-thumb.grid-responsive > div:nth-child(65) > div > div > a > img
    #// *[ @ id = "main-container"] / div / div[2] / div[65] / div / div / a / img

    imgs = soup.select('div > div > a > img')
    for img in imgs:
        data = {'image': img.get('src')}
        datas.append(data)

    return datas

def download(datas):
    for image in datas:
        localUrl = datas[image]
        urllib.request.urlretrieve

for url in urls:
    datas = get_page(url)
    time.sleep(2)
    print(datas)

