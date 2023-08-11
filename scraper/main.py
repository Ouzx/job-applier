import datetime
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

        self.expereince_index = 0  # 0: 1-2 years, 1: 2-5 years, 2: 5+ years

        self.jobs = []
        self.page = 0  # 1?

        now = datetime.datetime.now()
        self.log_file_name = f'logs/{now.strftime("%Y-%m-%d_%H-%M-%S")}_log.txt'
        self.log_chunk_size = 1000
        self.log_buffer = []

        self.print('Scraper initialized.')

    def scrape(self):
        self.print('Starting scraping...')

        self.driver.maximize_window()
        self.driver.get(self.link)

        # click cookie button
        # self.driver.find_element(
        #     By.CSS_SELECTOR, config.selectors['cookie_button']).click()

        # search jobs
        time.sleep(config.section_wait)
        self.search_jobs()

        time.sleep(config.section_wait)
        try:
            while self.is_next_page_available():
                self.print(f'Page: {self.page} - Scraping...')
                self.scrape_page()
                self.page += 1
        except Exception as e:
            self.print(f'Exception: {e}')
            self.print('Scraping stopped.')
        finally:
            self.quit()

    def scrape_page(self):
        # apply jobs
        time.sleep(config.section_wait)
        self.apply_jobs()

        # load more jobs
        time.sleep(config.section_wait)
        self.load_more_jobs()

    def search_jobs(self):
        self.print('Searching jobs...')

        # fill place
        self.driver.find_element(
            By.CSS_SELECTOR, config.selectors['place_text_box']).send_keys(config.place)
        time.sleep(config.fill_wait)
        self.driver.find_element(
            By.CSS_SELECTOR, config.selectors['place_text_box']).send_keys(Keys.ENTER)

        # fill tags
        self.driver.find_element(
            By.CSS_SELECTOR, config.selectors['tags_text_box']).send_keys(config.tags[0])
        for tag in config.tags[1:]:
            time.sleep(config.fill_wait)
            self.driver.find_element(
                By.CSS_SELECTOR, config.selectors['tags_text_box']).send_keys(Keys.ENTER)
            self.driver.find_element(
                By.CSS_SELECTOR, config.selectors['tags_text_box']).send_keys(tag)

        # click first experience buttons
        self.driver.find_elements(
            By.CSS_SELECTOR, config.selectors['expereince_buttons'])[0].click()

        # click match button
        self.driver.find_element(
            By.CSS_SELECTOR, config.selectors['match_button']).click()

    def is_next_page_available(self):
        try:
            is_available = self.driver.find_element(
                By.CSS_SELECTOR, config.selectors['next_page_button']).is_enabled()
            self.print(f'Next page is available: {is_available}')
            return is_available
        except:
            self.print('Next page is not available.')
            return False

    def apply_jobs(self):
        self.print('Applying jobs...')

        # get job list
        if self.page == 0:
            self.jobs = self.driver.find_elements(
                By.CSS_SELECTOR, config.selectors['job_result'])
        else:
            # results-page-divider-component:last-of-type ~ .result
            self.jobs = self.driver.find_elements(
                By.CSS_SELECTOR, f'{config.selectors["result_list_divider"]}:last-of-type ~ {config.selectors["job_result"]}')

        # if no jobs found, return
        if len(self.jobs) == 0:
            self.print('No jobs found. ')
            self.quit()

        self.print(f'Found {len(self.jobs)} jobs.')

        # apply jobs
        for job in self.jobs:
            time.sleep(config.section_wait)

            # click apply button
            job.find_element(
                By.CSS_SELECTOR, config.selectors['apply_button']).click()

            # fill email
            time.sleep(config.fill_wait)
            job.find_element(
                By.CSS_SELECTOR, config.selectors['email_input']).send_keys(config.email)

            # fill name
            time.sleep(config.fill_wait)
            job.find_element(
                By.CSS_SELECTOR, config.selectors['name_input']).send_keys(config.full_name)

            # attach resume
            time.sleep(config.fill_wait)
            job.find_element(
                By.CSS_SELECTOR, config.selectors['attach_resume_button']).send_keys(config.resume_path)

            # submit application
            time.sleep(config.fill_wait*2)
            job.find_element(
                By.CSS_SELECTOR, config.selectors['submit_button']).click()

            self.applied_job_count += 1
        self.print(f'Applied job #{self.applied_job_count}')

    def load_more_jobs(self):
        self.print('Loading more jobs...')
        self.driver.find_element(
            By.CSS_SELECTOR, config.selectors['next_page_button']).click()

    def print(self, *args, **kwargs):
        text = ' '.join(map(str, args))
        self.log_buffer.append(text)
        if len(self.log_buffer) >= self.log_chunk_size:
            self.save_log_chunk()

        # call the built-in print function with the same arguments
        built_in_print(*args, **kwargs)

    def save_log_chunk(self):
        with open(self.log_file_name, 'a+') as file:
            file.write('\n'.join(self.log_buffer) + '\n')
        self.log_buffer = []
        print('Saved log chunk. Buffer cleared.')

    def save_summary_log(self):
        with open('logs/log.txt', 'a+') as file:
            file.write(
                f'{self.applied_job_count} jobs applied. On {self.page} pages. With experience-level: {self.expereince_index} at: {time.ctime()} \n\n')
        print('Saved summary log.')

    def quit(self):
        print('Saving logs...')
        self.save_log_chunk()
        self.save_summary_log()
        print('Quitting...')
        self.driver.quit()

    @ staticmethod
    def __get_options():
        ua = UserAgent()
        userAgent = ua.random
        options = webdriver.ChromeOptions()
        options.add_argument(f'user-agent={userAgent}')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        return options


def built_in_print(*args, **kwargs):
    print(*args, **kwargs)
