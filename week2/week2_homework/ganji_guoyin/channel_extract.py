from bs4 import BeautifulSoup
import requests
import pymongo

start_url = 'http://bj.ganji.com/wu/'
url_add = 'http://bj.ganji.com'

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
page_link = ganji['page_link']

def get_channel_url(start_url, ):

    wb_data = requests.get(start_url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    urls = soup.select('dl.fenlei > dt > a')
    channel_url = []
    for url in urls:
        channel = url_add + url.get('href')
        channel_url.append(channel)
        print(channel)

    return channel_url

def get_link_url(page_url):
    page_url_set = [page_url + 'o{}'.format(i) for i in range(100)]

    for page in page_url_set:
        wb_data = requests.get(page)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        links = soup.select('li.js-item > a.ft-tit')
        for link in links:
            url = link.get('href')
            name = link.text.strip()
            data = {'name' : name,
                    'url' : url}
            print(data)
            if page_link.find(data).count() == 0:
                print('insert')
                page_link.insert_one(data)
            else:
                print('exist')
                continue





if __name__ == '__main__':
    # channel_url = get_channel_url(start_url)
    get_link_url('http://bj.ganji.com/jiaju/')