from argparse import Action
from selenium import webdriver
from time import sleep
import time
from datetime import datetime, date, time, timedelta

from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument("--headless")
driver = webdriver.Chrome(options=option)

driver.get("https://www.lambdatest.com/selenium-playground/iframe-demo")
#driver.maximize_window()
sleep(1)

iframe = driver.find_element(By.XPATH, '//*[@id="iFrame1"]')
driver.switch_to.frame(iframe)
textzone =  driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]')
sleep(2)
textzone.send_keys(Keys.CONTROL + "a")
textzone.send_keys(Keys.DELETE)
bold_button_iframe = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/button[1]')
x = "Шла Маша по шоссе"
textzone.send_keys(x)
textzone.send_keys(Keys.CONTROL + "a")
bold_button_iframe.click()




