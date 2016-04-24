from bs4 import BeautifulSoup
import string

path = 'index.html'
grades = []
with open(path, 'r') as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    print(wb_data)

    tittles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    reviews = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    stars = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p > span')
    while len(stars) != 0:
        sep_stars = stars[0:5]
        grades.append(sep_stars)
        del stars[0:5]
for tittle, image, price, review, grade in zip(tittles, images, prices, reviews, grades):
    data = {'title' : tittle.get_text(),
            'image': image.get('src'),
            'review': review.get_text(),
            'price': price.get_text(),
            'star': len(grad.find_all('span', class_='glyphicon glyphicon-star'))}
    print(data)




