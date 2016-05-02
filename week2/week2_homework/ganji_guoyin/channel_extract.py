from bs4 import BeautifulSoup
import requests
import pymongo

start_url = 'http://bj.ganji.com/wu/'
url_add = 'http://bj.ganji.com'

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




if __name__ == '__main__':
    channel_url = get_channel_url(start_url)