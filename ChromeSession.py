# coding: utf-8
# author:iiii706
#序列化session_id,如session_id不可以用，重新创建chrome实例并序列化session_id
#返回，一个可复用的chrome实例

import hashlib
import re
import pickle
import os
import sys
if sys.platform != 'linux':
    import win32com.client
from myChromeDriver import MyChromeWebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from datetime import datetime


class ChromeSession():
    def __init__(self):
        #os.startfile('chromedriver.exe')
        self.server_url = 'http://127.0.0.1:9515'
        #'args': ['--user-agent=iphone', '--headless']User-Agent和headless模式
        self.desired_capabilities = {'browserName': 'chrome', 'version': '', 'platform': 'ANY', 'goog:chromeOptions': {
            'prefs': {'profile.default_content_setting_values': {'images': 1, 'javascript': 1}}, 'extensions': [],
            'args': []}}

        if self.CheckProcExistByPN('chromedriver.exe') == 0:
            os.startfile('chromedriver.exe')

        try:
            # 反序列化
            with open('session_id.pkl', 'rb') as f:
                self.session_id = pickle.load(f)
            self.driver = MyChromeWebDriver(self.server_url,self.session_id)
            #print('########except###########')
            self.driver.get('https://www.httpbin.org/ip')
        except:
            #print('########new webdriver###########')
            self.driver = webdriver.Remote(command_executor='http://127.0.0.1:9515',
                                  desired_capabilities=self.desired_capabilities)
            with open('session_id.pkl', 'wb') as f:
                #print('# 序列化')
                pickle.dump(self.driver.session_id, f)
            self.sessiong_id = self.driver.session_id


    #检查是否已经启动chromedriver
    def CheckProcExistByPN(self,process_name):
        try:
            WMI = win32com.client.GetObject('winmgmts:')
            processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
        except Exception as e:
            print(process_name + "error : ", e)
        if len(processCodeCov) > 0:
            #print(process_name + " exist")
            return 1
        else:
            #print(process_name + " is not exist")
            return 0



if __name__ == '__main__':
    ChromeSession().driver


