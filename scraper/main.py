import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from fake_useragent import UserAgent

import scraper.strings as strs


class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome(options=self.__get_options())
        self.driver.get("https://www.google.com/")
        self.driver.maximize_window()

    def scrape(self):
        print('Scraping...')

    @ staticmethod
    def __get_options():
        ua = UserAgent()
        userAgent = ua.random
        options = webdriver.ChromeOptions()
        options.add_argument(f'user-agent={userAgent}')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        return options
