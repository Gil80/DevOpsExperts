from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import sys

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
get_title = driver.get("https://www.ynet.co.il")

if get_title == "ynet - חדשות, כלכלה, ספורט ובריאות - דיווחים שוטפים מהארץ ומהעולם":
    print("True")
else:
    print("False")
    
print(driver.title)
driver.quit()
