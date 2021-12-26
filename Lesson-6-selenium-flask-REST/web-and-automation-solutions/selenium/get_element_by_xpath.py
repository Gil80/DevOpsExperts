from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

my_drv = webdriver.Chrome(executable_path="/home/modi/dev/devops-experts/lesson_4/selenium/chromedriver")
my_drv.get('file:///home/modi/dev/devops-experts/lesson_4/tip_calc_orig/index.html')
print(my_drv.find_element(by="/html/body/div/div[1]/p[2]").text)
my_drv.close()


