from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
xiaozhu = client['xiaozhu']
hotel_price = xiaozhu['hotel_price']

urlSource = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(i) for i in range(1, 4)]
print(urlSource)


def gender_select(raw_gender):
    if raw_gender.get('class')[0] == '':
        return ''
    else:
        return raw_gender.get('class')[0].rsplit("_")[1]


def get_attributions(url):
    wb_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    title = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')[0].text
    position = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span.pr5')[0].text.strip()
    price = soup.select('#pricePart > div.day_l > span')[0].text
    image = soup.select('#curBigImage')[0].get('src')
    host_name = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')[0].get('title')
    host_image = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')[0].get('src')
    raw_gender = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')[0]
    host_gender = gender_select(raw_gender)

    data = {'title': title,
            'position': position,
            'price': price,
            'image': image,
            'host name': host_name,
            'host_image': host_image,
            'host_gender': host_gender}

    return data


# search main page

def get_info(urlSource, hotel_price, headers=None):
    for iSource in urlSource:
        home_data = requests.get(iSource)
        soup = BeautifulSoup(home_data.text, 'lxml')
        link = soup.select('#page_list > ul > li > a')
        price = soup.select('span.result_price > i')
        name = soup.select('.result_title')

        for iprice, ilink, iname in zip(price, link, name):
            localUrl = ilink.get('href')
            localPrice = int(iprice.text)
            localName = iname.text
            # print(localUrl, localPrice, localName)

            data = {'name': localName,
                    'price': localPrice,
                    'link': localUrl}
            if not hotel_price.find(data):
                hotel_price.insert_one(data)

        return


def check_db(hotel_price, price=500):
    for house in hotel_price.find({"price": {"$gt": '100'}}):
        print(house)
    return


get_info(urlSource, hotel_price)
check_db(hotel_price)
