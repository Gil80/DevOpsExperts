# pip install selenium
# pip install webdriver_manager

from selenium import webdriver


def chrome():
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--disable-dev-shm-using")
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.headless = True
    driver.get('https://www.walla.co.il')
    print(driver.title)
    driver.quit()


def firefox():
    from webdriver_manager.firefox import GeckoDriverManager
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("https://www.ynet.co.il")
    print(driver.title)
    driver.quit()


chrome()
firefox()
