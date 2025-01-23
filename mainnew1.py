from selenium import webdriver
from time import sleep
import datetime

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

file = open("lognew.txt", "w")

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument("--headless")
driver = webdriver.Chrome(options=option)

driver.get("http://demoqa.com/checkbox")
driver.maximize_window()


main_list = driver.find_element(By.XPATH,  '//*[@id="tree-node"]/div/button[1]')
main_list.click()
home_check_box = driver.find_element(By.XPATH,  '//*[@id="tree-node"]/ol/li/ol/li[1]/span/label')
home_check_box.click()
sleep(2)
home_check_box.click()

file.close()