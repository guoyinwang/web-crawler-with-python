from bs4 import BeautifulSoup
import requests
import time


urlSource = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(i) for i in range(1,10 )]
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



    data = {'title' : title,
            'position' : position,
            'price' : price,
            'image' : image,
            'host name' : host_name,
            'host_image' : host_image,
            'host_gender' : host_gender}

    return data






results = []

for iSource in urlSource:
    home_data = requests.get(iSource)
    soup = BeautifulSoup(home_data.text, 'lxml')
    link = soup.select('#page_list > ul > li > a')

    for ilink in link:
        localUrl = ilink.get('href')
        print(localUrl)
        local_data = get_attributions(localUrl)
        results.append(local_data)

print(results)



