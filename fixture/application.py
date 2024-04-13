import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from assertpy import assert_that

from fixture.demonstration_app_demo_qa import DemonstrationAppDemoQa
from fixture.orange_hrm import OrangeHrm
from fixture.step import StepHelper
from helpers.utils import Utils


class Application:

    def __init__(self, headless=False):
        service = Service()
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("user-agent='User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'")
        self.wd: webdriver = webdriver.Chrome(service=service, options=chrome_options)
        self.wd.get_window_size('1920,1080')

        self.assert_that = assert_that
        self.step = StepHelper(self)
        self.orangeHrm = OrangeHrm(self)
        self.demonstrationAppDemoQa = DemonstrationAppDemoQa(self)
        self.utils = Utils(self)

    def destroy(self):
        self.wd.quit()