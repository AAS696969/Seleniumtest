from argparse import Action
from selenium import webdriver
from time import sleep
import time
from datetime import datetime, date, time, timedelta

from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from newmain3 import action

# file = open("lognew.txt", "w")

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument("--headless")
driver = webdriver.Chrome(options=option)

driver.get("https://html5css.ru/howto/howto_js_rangeslider.php")
driver.maximize_window()
sleep(1)

slider = driver.find_element(By.XPATH, '//*[@id="id2"]')
action =ActionChains(driver)
sleep(2)
action.click_and_hold(slider).move_by_offset(-50,0).release().perform()

# file.close()
