import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from fake_useragent import UserAgent

import config.main as config


class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome(options=self.__get_options())

        self.applied_job_count = 0
        self.link = config.link

        self.jobs = []
        self.page = 0  # 1?

    def scrape(self):
        self.driver.get(self.link)
        self.driver.maximize_window()
        print('Scraping...')

    def quit(self):
        self.driver.quit()

    @ staticmethod
    def __get_options():
        ua = UserAgent()
        userAgent = ua.random
        options = webdriver.ChromeOptions()
        options.add_argument(f'user-agent={userAgent}')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        return options
