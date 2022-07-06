# coding: utf-8
# author:iiii706

#实现复用已经打开的webdriver
import warnings
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.chrome.remote_connection import ChromeRemoteConnection,RemoteConnection
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.errorhandler import ErrorHandler
from selenium.webdriver.remote.switch_to import SwitchTo
from selenium.webdriver.remote.mobile import Mobile
from selenium.webdriver.remote.file_detector import FileDetector, LocalFileDetector
from selenium.webdriver.remote.command import Command

class MyChromeWebDriver(WebDriver):

    def __init__(self, service_url=None, session_id=None):

        if service_url is None and session_id is None:
            raise NameError

        self.w3c = True
        executor = ChromeRemoteConnection(remote_server_addr=service_url)
        self.session_id = session_id
        #print('self.session_id',self.session_id)
        self.session_id = session_id
        self.command_executor = executor
        self.command_executor.w3c = self.w3c
        if type(self.command_executor) is bytes or isinstance(self.command_executor, str):
            self.command_executor = RemoteConnection(self.command_executor, keep_alive=True)
        self._is_remote = True
        self.error_handler = ErrorHandler()
        self._switch_to = SwitchTo(self)
        self._mobile = Mobile(self)
        self.file_detector = LocalFileDetector()

    def launch_app(self, id):
        """Launches Chrome app specified by id."""
        return self.execute("launchApp", {'id': id})

    def get_network_conditions(self):

        return self.execute("getNetworkConditions")['value']

    def set_network_conditions(self, **network_conditions):

        self.execute("setNetworkConditions", {
            'network_conditions': network_conditions
        })

    def quit(self):
        try:
            RemoteWebDriver.quit(self)
        except Exception:
            # We don't care about the message because something probably has gone wrong
            pass
        finally:
            self.service.stop()

    def create_options(self):
        return Options()

