from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

my_drv = webdriver.Chrome(executable_path="/home/gil/projects/DevOpsExperts/Lesson-6/tip_calc/chromedriver_linux64/chromedriver")
my_drv.get('/home/gil/projects/DevOpsExperts/Lesson-6/tip_calc/index.html')
print(my_drv.find_element(by=By.XPATH, value="/html/body/div/div[1]/p[2]").text)
my_drv.close()
