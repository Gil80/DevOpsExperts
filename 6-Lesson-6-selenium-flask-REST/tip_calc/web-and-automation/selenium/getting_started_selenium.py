import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options,
                           executable_path="/home/gil/projects/DevOpsExperts/Lesson-6/tip_calc/chromedriver_linux64/chromedriver")
browser.get("https://www.google.com")
print(browser.title)

for i in range(0, 5):
    sleep(5)
    browser.close()
