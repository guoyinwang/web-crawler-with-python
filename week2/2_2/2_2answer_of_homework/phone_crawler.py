from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
phone58 = client['phone58']
url_list = phone58['url_list']
# url_list.remove()
item_info = phone58['item_info']


url = 'http://bj.58.com/shoujihao/'
url_set = ['http://bj.58.com/shoujihao/pn{}'.format(i) for i in range(1, 100)]

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
        # if not url_list.find(data):
            # print('not found')
        url_list.insert_one(data)


def get_all_links(url_set):
    for url in url_set:
        print(url)
        get_links(url)
        time.sleep(2)




# spider 2
def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    no_longer_exist = '404' in soup.find('script', type="text/javascript").get('src').split('/')
    if no_longer_exist:
        pass
    else:
        title = soup.select('div.col_sub.mainTitle > h1')[0].text.strip().split('\n')[0]
        price = soup.select('span.price.c_f50')[0].text.strip()
        area = [soup.select('div.su_con > a')[i].text for i in range(0,len(soup.select('div.su_con > a')))] if len(soup.select('div.su_con > a')) > 0 else None
        seller_name = soup.select('a.tx')[0].text
        seller_link = soup.select('a.tx')[0].get('href')
        contact = soup.select('span.f20')[0].text.strip()

        data = {'title' : title,
                'price' : price,
                'area' : area,
                'seller_name' : seller_name,
                'seller_link' : seller_link,
                'contact' : contact}
        print(data)
        item_info.insert_one(data)


# main part
if __name__ == '__main__':
    get_all_links(url_set)
    for item in url_list.find():
        item_link = item['link']
        get_item_info(item_link)
        time.sleep(2)





# get_item_info('http://bj.58.com/shoujihao/25855401860426x.shtml?psid=179488680191631706474196179&entinfo=25855401860426_0&iuType=p_2&PGTID=0d3000f1-0000-1294-9bbc-2c03c0eff678&ClickID=1')

