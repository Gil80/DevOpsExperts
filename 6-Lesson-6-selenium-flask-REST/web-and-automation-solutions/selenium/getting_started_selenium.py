from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path="/home/modi/dev/devops-experts/lesson_4/selenium/chromedriver")
browser.get("https://www.google.com")
print(browser.title)

from time import sleep
sleep(5)

browser.close()
