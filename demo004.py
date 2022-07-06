import cloudscraper
from datetime import datetime
scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'android',
        'desktop': False,
        'mobile': True,

    }
)
start = datetime.now()
#scraper = cloudscraper.create_scraper()
page = scraper.get('https://www.amazon.com/PIMCAR-Organizer-Compatible-Silverado-Accessories/dp/B085XZTVKH')
print(page.status_code)
with open('asin1.html','a+',encoding='utf-8') as f:
    f.write(page.text)

end = datetime.now()
print('用时：',end-start)