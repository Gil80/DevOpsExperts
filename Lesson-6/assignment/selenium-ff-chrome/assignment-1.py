import os
import logging

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver import firefox

logging.getLogger().setLevel(logging.INFO)

CHROME_URL = 'http://www.walla.co.il'
FF_URL = 'http://www.ynet.co.il'


def chrome_example():
    print("Using Chrom...")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-using")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.headless = True
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(CHROME_URL)
    print('Accessed ..', CHROME_URL)
    print('Page title: ', browser.title)
    browser.quit()


def firefox_example():
    print("Using Firefox...")
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.add_argument("-headless")
    browser = webdriver.Firefox(options=options)
    browser.get(FF_URL)
    print('Page title: ', browser.title)
    browser.quit()


if __name__ == '__main__':
    chrome_example()
    firefox_example()