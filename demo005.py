import cloudscraper
from datetime import datetime
from lxml import etree
scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'android',
        'desktop': True,
    }
)
headers ={
    "accept": "text/html, application/json",
    "accept-language": "en,en-US;q=0.3",
    "content-type": "application/json",
    # "device-memory": "8",
    # "downlink": "1.5",
    # "dpr": "1",
    # "ect": "4g",
    # "rtt": "200",
    # "sec-ch-device-memory": "8",
    # "sec-ch-dpr": "1",
    # "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\", \"Google Chrome\";v=\"101\"",
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "\"Windows\"",
    # "sec-ch-viewport-width": "1920",
    # "sec-fetch-dest": "empty",
    # "sec-fetch-mode": "cors",
    # "sec-fetch-site": "same-origin",
    # "viewport-width": "1920",
    "x-amz-acp-params": "tok=INeeROdRUqD035Sk-C62qrzWOnBmT_vdn5Qy7XZL5RM;ts=1652324602645;rid=M5AR42DZ1REN6CRMXSAE;d1=629;d2=0",
    "x-requested-with": "XMLHttpRequest",
    #"cookie": "session-id=145-1811831-0420629; session-id-time=2082787201l; i18n-prefs=USD; ubid-main=131-6322341-0784058; lc-main=en_US; session-token=\"QpvNsWTfbYNFZs19g/ni/nblfl8mz7TCSnbjnyPJefx+SOEKO+gIxm4X3pfFJWe9akleafqiXtwSvRAkWj9bZsMSxXrJSP9RSvfpe+swkFNVeWC0nUisT4U8VhF4GFemjrJdOc1+kFthHTVzKO9aNv3f8iUWvUBZd+19khhDaIcVBs4Ah6olzm0pXe3lTsiE7Z+kYg6rytGOBuzrqGkzDw==\"; csm-hit=tb:NC7GKDM9SQ8BCFY9MC7B+s-M5AR42DZ1REN6CRMXSAE|1652324875953&t:1652324875953&adb:adblk_no",
    "Referer": "https://www.amazon.com/gp/bestsellers/automotive/15710141/ref=pd_zg_hrsr_automotive",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }

url = 'https://www.amazon.com/acp/p13n-zg-list-grid-desktop/qqw1dr01f0cvb9mu/nextPage?'

data = '''
{\"faceoutkataname\":\"GeneralFaceout\",\"ids\":[\"{\\\"id\\\":\\\"B09VC5R77H\\\",\\\"metadataMap\\\":{\\\"render.zg.rank\\\":\\\"1\\\",\\\"render.zg.bsms.currentSalesRank\\\":\\\"\\\",\\\"render.zg.bsms.percentageChange\\\":\\\"\\\",\\\"render.zg.bsms.twentyFourHourOldSalesRank\\\":\\\"\\\"},\\\"linkParameters\\\":{}}\"],\"indexes\":[1],\"linkparameters\":\"\",\"offset\":\"1\",\"reftagprefix\":\"\"}'''
res = scraper.post(url,data=data,headers=headers)
print(res.status_code)
html = res.content
html_srt = str(html,encoding='utf-8')
print(html_srt)
html_srt = html_srt.replace('href="','target="_blank" href="https://www.amazon.com/')
selector = etree.HTML(html_srt)


with open('asin123.html','a+',encoding='utf-8') as f:
    f.write(html_srt)