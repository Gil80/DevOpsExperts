#Yes they are the same.
#Open google.com and look at the search field element. The name of the fiels is 'q' in every browser.

import os
import logging

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver import firefox

logging.getLogger().setLevel(logging.INFO)

CHROME_URL = 'http://www.google.com'
FF_URL = 'http://www.google.com'


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
    search_field = browser.find_element_by_name('q') 
    search_field.send_keys("some text")
    browser.quit()


def firefox_example():
    print("Using Firefox...")
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.add_argument("-headless")
    browser = webdriver.Firefox(options=options)
    browser.get(FF_URL)
    print('Page title: ', browser.title)
    search_field = browser.find_element_by_name('q') 
    search_field.send_keys("some text")
    browser.quit()


if __name__ == '__main__':
    chrome_example()
    firefox_example()