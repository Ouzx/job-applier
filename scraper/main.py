import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from fake_useragent import UserAgent

import scraper.strings as strs


class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome(options=self.__get_options())

        self.applied_job_count = 0
        self.link = Scraper.get_base_link()

        self.jobs = []
        self.page = 0  # 1?

    def scrape(self):
        self.driver.get(self.link)
        self.driver.maximize_window()
        print('Scraping...')

    @ staticmethod
    def get_base_link():
        with open(strs.link_path, "r") as f:
            return f.read()

    @ staticmethod
    def __get_options():
        ua = UserAgent()
        userAgent = ua.random
        options = webdriver.ChromeOptions()
        options.add_argument(f'user-agent={userAgent}')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        return options
