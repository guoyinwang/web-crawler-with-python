from bs4 import BeautifulSoup
import requests
import urllib
import time

urlMain = 'http://bj.58.com/pbdn/0/'

url = 'http://bj.58.com/pingbandiannao/25669149490503x.shtml'
# api =  http://jst1.58.com/counter?infoid=25669149490503&userid=&uname=&sid=514968980&lid=1&px=512862527&cfpath=5,38484

header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36'}

def get_count(url):
    usr_id = url.split('/')[-1].strip('x.shtml')
    api = 'http://jst1.58.com/counter?infoid={}'.format(usr_id)
    js = requests.get(api)
    print(js.text)
    views = js.text.split('=')[-1]
    print(views)
    return views

def get_info(url, header = None):
    web_data = requests.get(url, headers = header)
    soup = BeautifulSoup(web_data.text, 'lxml')

    title = soup.select('div.col_sub.mainTitle > h1')[0].text
    cate = soup.select('span.crb_i > a')[0].text
    time = soup.select('li.time')[0].text
    price = soup.select('div.su_con > span')[0].text
    quality = soup.select('div.su_con > span')[1].text.strip()
    region = soup.select('div.su_con > span.c_25d > a')[0].text if soup.find_all('span','c_25d') else None
    totalCount = get_count(url)

    data = {'title' : title,
            'category' : cate,
            'time' : time,
            'price' : price,
            'quality' : quality,
            'region' : region,
            'count' : totalCount}

    print(title)
    print(cate)
    print(time)
    print(price)
    print(quality)
    print(region)
    print(totalCount)
    return data

def get_root_page(url, header = None):
    web_data = requests.get(url, headers=header)
    soup = BeautifulSoup(web_data.text, 'lxml')

    links = soup.select('div.cleft > table.tbimg > tr > td.t > a.t')
    link_zz = soup.select('tr.zzinfo > td.t > a.t')

    urlSet = []
    for url in links:
        if  url not in link_zz:
            urlSet.append(url.get('href').split('?')[0])

    return urlSet

def main_scrapy(url, header = None):
    urls = get_root_page(url, header)
    datas = []

    for url in urls:
        data = get_info(url, header)
        time.sleep(2)
        datas.append(data)
    print(datas)
    return datas



get_info(url, header)
# main_scrapy(urlMain, header = header)



