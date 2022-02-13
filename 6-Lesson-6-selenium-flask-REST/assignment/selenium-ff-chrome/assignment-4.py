
import os
import logging
from time import sleep

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver import firefox

logging.getLogger().setLevel(logging.INFO)

CHROME_URL = 'https://translate.google.com/?sl=iw&tl=en&op=translate'


def chrome_example():
    print("Using Chrom...")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-using")
    chrome_options.add_argument("--disable-extensions")
    #chrome_options.headless = True
    browser = webdriver.Chrome(chrome_options=chrome_options,executable_path="/home/gil/projects/DevOpsExperts/Lesson-6/assignment/selenium-ff-chrome/chromedriver")
    browser.get(CHROME_URL)
    print('Accessed ..', CHROME_URL)
    print('Page title: ', browser.title)
    search_field = browser.find_element_by_tag_name('textarea') 
    search_field.send_keys("החלק הכי קשה בלימודי רוקחות, זה ההתאסלמות.")
    sleep(10)
    browser.close


if __name__ == '__main__':
    chrome_example()