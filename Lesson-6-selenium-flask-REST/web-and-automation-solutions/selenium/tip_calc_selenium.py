from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-dev-shm-using")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument(r"user-data-dir=.\cookies\\test")
chromeOptions.headless = True
browser = webdriver.Chrome(chrome_options=chromeOptions)
browser.get('file:///external/tip_calc/index.html')
sleep(1)
browser.find_element(by=By.ID, value='billamt').send_keys("100")
sleep(1)
select = Select(browser.find_element(by=By.ID, value='serviceQual'))
sleep(1)

# select by visible text
select.select_by_value('0.3')
sleep(1)
browser.find_element(by=By.ID, value="music-quality").send_keys("4")
sleep(1)
browser.find_element(by=By.ID, value="peopleamt").send_keys("4")
sleep(1)
browser.find_element(by=By.ID, value="calculate").click()
sleep(1)
actual = browser.find_element(by=By.ID, value="tip").text
print("actual: {0}".format(actual))
expected = "11.50"
assert actual == expected, "Error"
sleep(2)
browser.close()