import time
from channel_extract import page_link
from page_parsing import page_info

while True:
    print('page link number is ', page_link.find().count())
    print('page info number is ', page_info.find().count())
    time.sleep(5)
