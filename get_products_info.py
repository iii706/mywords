import cloudscraper
from datetime import datetime
import time,random
from lxml import etree

#获取上架时间
def get_date_first_available(selector):
    xpath_arrs = [
        '//span[contains(*,"Date First Available")]//text()',
        '//tr[contains(*,"Date First Available")]//text()'
    ]
    replace_strs = ['\n',':','Date First Available','                                 ','\u200e','\u200f']
    for xpath_arr in xpath_arrs:
        up_date = selector.xpath(xpath_arr)
        if len(up_date) > 0 :
            up_date = ''.join(up_date)
            for replace_str in replace_strs:
                up_date = up_date.replace(replace_str,'').strip()
            return up_date.strip()
    return ''

#获取排名rank
def get_product_rank(selector):
    xpath_arrs = [
        '//span[contains(*,"Best Sellers Rank")]//text()',
        '//tr[contains(*,"Best Sellers Rank")]//text()'
    ]
    replace_strs = ['\n','Best Sellers Rank',':']
    for xpath_arr in xpath_arrs:
        rank_text = selector.xpath(xpath_arr)
        if len(rank_text) > 0 :
            rank_text = ''.join(rank_text).split('(See')[0]
            for replace_str in replace_strs:
                rank_text = rank_text.replace(replace_str,'').strip()
            rank_text = rank_text.split(' in ')
            rank = rank_text[0].replace('#','').replace(',','')
            cat = rank_text[1]
            return rank.strip(),cat.strip()
    return 999999,'#NA'

page_start = 1 #首页
page_end = 100 #尾页

review_count = 300 #小于300
up_year = 2021 #上架时间在2021后
set_rank = 50000 #在大类目50000名内
filter_words_in_title = ['Mask','Masks'] #过滤标题关键词，如口罩


for page in range(page_start,page_end):
    if page == 1:
        url = 'https://www.amazon.com/s?k=made+in+usa&i=kitchen&rh=n%3A284507&dc&page='+str(page)+'&crid=29NW53ZKVYBMP&qid=1652338068&rnid=2941120011&sprefix=made+in+usa%2Caps%2C565&ref=sr_pg_'+str(page)
    else:
        url = 'https://www.amazon.com/s?k=made+in+usa&i=kitchen&rh=n%3A284507&dc&page=' + str(
            page) + '&crid=29NW53ZKVYBMP&qid=1652338068&rnid=2941120011&sprefix=made+in+usa%2Caps%2C565&ref=sr_pg_' + str(
            page-1)
    scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'chrome',
            'platform': 'linux',
            'desktop': True,
            # 'mobile': True,

        }
    )
    res = scraper.get(url)
    print('第%s页打开中...'%str(page),res.status_code)

    selector = etree.HTML(res.text)
    products_eles = selector.xpath('//div[@data-component-type="s-search-result"]')
    for products_ele in products_eles:
        texts = ''.join(products_ele.xpath('.//text()'))
        if texts.find('You’re seeing this ad based on the produc') != -1:
            continue
        title = ''.join(products_ele.xpath('.//span[@class="a-size-base-plus a-color-base a-text-normal"]/text()'))

        #剔除过滤的关键词
        filter_word_flag = 0
        for filter_word_in_title in filter_words_in_title:
            if texts.find(filter_word_in_title) != -1: #剔除口罩关键词
                filter_word_flag = 1
                break
        if filter_word_flag:
            continue

        reviews = ''.join(products_ele.xpath('.//span[@class="a-size-base s-underline-text"]/text()')).replace(',','')
        price = ''.join(products_ele.xpath('.//span[@class="a-price"]/span/text()')).replace('$','')
        asin = ''.join(products_ele.xpath('./@data-asin'))

        if reviews == '':
            reviews = '0'
        if int(reviews) < review_count:
            scraper1 = cloudscraper.create_scraper(
                browser={
                    'browser': 'chrome',
                    'platform': 'windows',
                    'desktop': True,
                    #'mobile': True,
                }
            )
            product_detail_res = scraper1.get('https://www.amazon.com/dp/' + asin)
            product_detail_selector = etree.HTML(product_detail_res.text)
            date_first_available = get_date_first_available(product_detail_selector)

            rank,cat = get_product_rank(product_detail_selector)
            print([asin,date_first_available,rank,cat,reviews,price])
            if date_first_available.find(',') != -1:
                year = date_first_available.split(',')[-1]
                if int(year) >= up_year and int(rank) < 50000:
                    data = ['https://www.amazon.com/dp/' + asin,date_first_available,rank,cat, title, reviews, price]
                    print(data)
                    with open('数据保存.txt','a+',encoding='utf-8') as f:
                        f.write('||'.join(data)+'\n')





