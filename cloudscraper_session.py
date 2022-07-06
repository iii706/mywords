import cloudscraper

from datetime import datetime
from lxml import etree

scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'windows',
        'desktop': True,
    })
scraper.headers['Accept'] = 'text/html'
#scraper.headers['Accept-Encoding'] = 'gzip'
print(scraper.headers)
start = datetime.now()
#scraper = cloudscraper.create_scraper()
page = scraper.get('https://www.amazon.com/sp?ie=UTF8&seller=AQ42PCCCJJV81&isAmazonFulfilled=1')
print(page.status_code)
#print(page.text)
# with open('asin1.html','a+',encoding='utf-8') as f:
#     f.write(page.text)
end = datetime.now()
print('用时：',end-start)