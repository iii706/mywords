from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from lxml import etree
import time
chrome_option = Options()
prefs = {
    'profile.default_content_setting_values': {
        'images': 2,
        'permissions.default.stylesheet': 2,
        'javascript': 2
    }
}
chrome_option.add_experimental_option('prefs', prefs)
chrome_option.add_argument('--no-sandbox')
chrome_option.add_argument('--disble-gpu')
#chrome_option.add_argument('--headless')
chrome_option.add_argument('window-size=1200x600')
chrome_option.add_experimental_option("excludeSwitches", ['enable-automation'])
browser = Chrome(options=chrome_option)
with open('stealth.min.js', 'r') as f:
    js = f.read()
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": js})
f =  open('topwords.txt','a+',encoding='utf-8')
wait = WebDriverWait(browser, 15)
words_heads = ['搜索词','本周排名','上周排名','排名涨跌']
f.write('|'.join(words_heads)+'\n')
str = 'abcdefghijklmnopqrstuvwxyz'
for i in str:
    for page in range(1,18):
        words_url = 'https://www.amz123.com/usatopkeywords-%s-1-%s.htm?rank=50000&uprank='%(page,i)
        browser.get(words_url)
        wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '.pagination'))
        )
        selector = etree.HTML(browser.page_source)

        list_datas = selector.xpath('//div[@class="listdata"]')


        for list_data in list_datas:
            trs = []
            for divs in list_data.xpath('.//text()'):
                if divs.strip() != '':
                    trs.append(divs.strip())
            f.write('|'.join(trs)+'\n')

        time.sleep(1)



f.close()
# url = 'https://www.merchantwords.com/search/us/usb cable/sort-highest'
# head_tr = ['AMAZON SEARCH','SEARCH VOLUME','3M AVG','12M AVG','DEPTH','RESULTS','SPONSORED ADS','PAGE 1 REVIEWS','APPEARANCE','LAST SEEN','CAT']
# #
# # browser.get(url)
# #
# # wait.until(
# #     ec.presence_of_element_located((By.CSS_SELECTOR, '#resultsTable'))
# # )
# # tr = []
# #
# # tr_eles = browser.find_elements_by_css_selector('#resultsTable > tbody > tr:nth-child(-n + 3)')
# # for tr_ele in tr_eles:
# #     td_eles = tr_ele.find_elements_by_css_selector('td')
# #     td_arr = []
# #     for td_ele in td_eles:
# #         ret_text = td_ele.text.replace('\nP1','')
# #         if ret_text != '':
# #             td_arr.append(ret_text)
# #     print(td_arr)
browser.close()

