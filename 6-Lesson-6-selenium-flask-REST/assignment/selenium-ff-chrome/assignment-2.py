import os
import logging

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver import firefox

logging.getLogger().setLevel(logging.INFO)

CHROME_URL = 'http://www.walla.co.il'
FF_URL = 'http://www.ynet.co.il'


def chrome_example():
    title = ''
    print("Using Chrom...")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-using")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.headless = True
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(CHROME_URL)
    print('Page title: ', browser.title)
    title = browser.title
    print('Accessed ..', CHROME_URL)
    browser.refresh
    if title == 'וואלה! - האתר המוביל בישראל - עדכונים מסביב לשעון':
        print("equal")
    else:
        print("not equal")
    browser.quit()


def firefox_example():
    title = ''
    print("Using Firefox...")
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.add_argument("-headless")
    browser = webdriver.Firefox(options=options)
    browser.get(FF_URL)
    print('Page title: ', browser.title)
    title = browser.title
    print('Accessed ..', CHROME_URL)
    browser.refresh
    if title == 'ynet - חדשות, כלכלה, ספורט ובריאות - דיווחים שוטפים מהארץ ומהעולם':
        print("equal")
    else:
        print("not equal")
    browser.quit()



if __name__ == '__main__':
    chrome_example()
    firefox_example()