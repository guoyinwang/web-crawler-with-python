from bs4 import BeautifulSoup
import requests
import urllib

urlMain = 'http://bj.58.com/pbdn/0/'

url = 'http://bj.58.com/pingbandiannao/25669149490503x.shtml?psid=164603488191565816143598655&entinfo=25669149490503_0&iuType=p_0&PGTID=0d305a36-0000-1633-39b7-238dc5bf7d6d&ClickID=2'
# http://jst1.58.com/counter?infoid=25669149490503&userid=&uname=&sid=514968980&lid=1&px=512862527&cfpath=5,38484

header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36'}
def get_info(url, header = None):
    #body > div.box.wrapper.clearfix > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > ul > li.price_li > span.price_now > i
    web_data = requests.get(url, headers = header)
    soup = BeautifulSoup(web_data.text, 'lxml')

    # content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.mainTitle > h1
    # header > div.breadCrumb.f12 > span:nth-child(3) > a
    # index_show > ul.mtit_con_left.fl > li.time
    # content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-child(1) > div.su_con > span
    # content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-child(2) > div.su_con > span
    # totalcount

    title = soup.select('div.col_sub.mainTitle > h1')[0].text
    cate = soup.select('span > a')[-2].text
    time = soup.select('li.time')[0].text
    price = soup.select('div.su_con > span')[0].text
    quality = soup.select('div.su_con > span')[1].text
    region = soup.select('div.su_con > span')[2].text
    totalCount = ('totalcount')

    data = {'title' : title,
            'category' : cate,
            'time' : time,
            'price' : price,
            'quality' : quality,
            'region' : region}

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
    # infolist > table:nth-child(8) > tbody > tr.zzinfo > td.t > a
    # infolist > table:nth-child(5) > tbody > tr > td.t > a

    # jingzhun > tbody > tr:nth-child(3) > td.t > a.t
    link = soup.select('div.cleft > table.tbimg > tr > td.t > a.t')
    link_zz = soup.select('tr.zzinfo > td.t > a.t')

    print(link)
    # print(link_zz)



# get_info(url, header)
get_root_page(urlMain, header = header)



