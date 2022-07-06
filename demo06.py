import cloudscraper
from datetime import datetime
from lxml import etree
scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'android',
        'desktop': False,
        'mobile': True,

    })
scraper.headers['Accept'] = 'text/html'
scraper.headers['x-amz-acp-params'] = 'tok=INeeROdRUqD035Sk-C62qrzWOnBmT_vdn5Qy7XZL5RM;ts=1652324602645;rid=M5AR42DZ1REN6CRMXSAE;d1=629;d2=0'
print(scraper.headers)
start = datetime.now()
data = '''
{\"faceoutkataname\":\"GeneralFaceout\",\"ids\":[\"{\\\"id\\\":\\\"B085XZTVKH\\\",\\\"metadataMap\\\":{\\\"render.zg.rank\\\":\\\"1\\\",\\\"render.zg.bsms.currentSalesRank\\\":\\\"\\\",\\\"render.zg.bsms.percentageChange\\\":\\\"\\\",\\\"render.zg.bsms.twentyFourHourOldSalesRank\\\":\\\"\\\"},\\\"linkParameters\\\":{}}\"],\"indexes\":[1],\"linkparameters\":\"\",\"offset\":\"1\",\"reftagprefix\":\"\"}'''

url = 'https://www.amazon.com/acp/p13n-zg-list-grid-desktop/qqw1dr01f0cvb9mu/nextPage?'

res = scraper.post(url,data=data)
print(res.status_code)
html = res.content
html_srt = str(html,encoding='utf-8')
print(html_srt)
html_srt = html_srt.replace('href="','target="_blank" href="https://www.amazon.com/')
selector = etree.HTML(html_srt)


with open('asin0528001.html','a+',encoding='utf-8') as f:
    f.write(html_srt)

end = datetime.now()
print('用时：',end-start)