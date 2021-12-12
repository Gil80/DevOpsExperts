from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-dev-shm-using")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.headless = True
chrome_driver = webdriver.Chrome(chrome_options=chromeOptions)

get_title = chrome_driver.get('https://www.walla.co.il')

chrome_driver.refresh()
if get_title == "וואלה! - האתר המוביל בישראל - עדכונים מסביב לשעון":
    print("True")
else:
    print("False")
    
print(chrome_driver.title)
chrome_driver.quit()
