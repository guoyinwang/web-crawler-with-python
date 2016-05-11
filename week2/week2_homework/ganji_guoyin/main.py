from multiprocessing import Pool
from channel_extract import ganji, get_channel_url, get_link_url
from page_parsing import page_parsing

db_item = [item['url'] for item in ganji['page_link'].find()]
finish_link = [item['url'] for item in ganji['page_info'].find()]

db_set = set(db_item)
finish_set = set(finish_link)

rest_set = db_set - finish_set

if __name__ == '__main__':
    operation= 2
    # step 1
    if operation == 1:
        start_url = 'http://bj.ganji.com/wu/'
        url_add = 'http://bj.ganji.com'
        channel_url = get_channel_url(start_url, url_add)

        # step 2
        pool = Pool(processes=4)
        pool.map(get_link_url, [url_item for url_item in channel_url])

        rest_set = set([item['url'] for item in ganji['page_link'].find()])
        pool.close()
        pool.join()

    # step 3
    pool = Pool(processes=4)
    pool.map(page_parsing, [page_item for page_item in rest_set])
    pool.close()
    pool.join()



