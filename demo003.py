from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from lxml import etree
import time
from ChromeSession import ChromeSession

url = 'https://m.qlchat.com/topic/details?topicId=2000012683025028'

# chrome_option = Options()
# prefs = {
#     'profile.default_content_setting_values': {
#         'images': 1,
#         'permissions.default.stylesheet': 1,
#         'javascript': 1
#     }
# }
#
# chrome_option.add_experimental_option('prefs', prefs)
# chrome_option.add_argument('--no-sandbox')
# chrome_option.add_argument('--disble-gpu')
# #chrome_option.add_argument('--headless')
# chrome_option.add_argument('window-size=1200x600')
# chrome_option.add_experimental_option("excludeSwitches", ['enable-automation'])
# #chrome_option.binary_location = r"C:\Chrome\chrome.exe"
#
# browser = Chrome(options=chrome_option)
#
# browser.get(url)

browser = ChromeSession().driver
browser.get(url)
wait = WebDriverWait(browser, 15)
print(browser.title)
time.sleep(10)
if browser.title == "知识店铺":
    wait.until(
        ec.presence_of_element_located((By.CSS_SELECTOR, 'body > div > div.container > div.login-type-box > ul > li:nth-child(1)'))
    )
    browser.find_element_by_css_selector('body > div > div.container > div.login-type-box > ul > li:nth-child(1)').click()
    user_name = browser.find_element_by_css_selector('#pwdLogin > form > div > div:nth-child(1) > input[type=tel]')
    user_name.clear()
    user_name.send_keys('13527782211')
    time.sleep(1)
    pwd = browser.find_element_by_css_selector('#pwdLogin > form > div > div:nth-child(2) > input')
    pwd.clear()
    pwd.send_keys('cjy123456')
    time.sleep(1)
    browser.find_element_by_css_selector('#pwdLogin > form > button').click()
    time.sleep(2)
    print(browser.title)
    time.sleep(10)

    try:
        browser.find_element_by_css_selector('#app > div:nth-child(1) > span > span.portal-high > div > div.bottom > div.close').click()
    except Exception as e:
        print(e)
    # with open('index.html','a+',encoding='utf-8') as f:
    #     f.write(browser.page_source)
msg_eles = browser.find_elements_by_css_selector('#main-scroll-area > div > div > div > span.flex-box > span')
for msg_ele in msg_eles:
    msg_ele.click()
    time.sleep(3)
    msgaudio = browser.find_element_by_css_selector('body > audio:nth-child(12)').get_attribute('src')
    print(msg_ele.text,msgaudio)



#browser.close()

