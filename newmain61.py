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

driver.get("https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo")
driver.maximize_window()
sleep(1)

click_drop = driver.find_element(By.XPATH, '//*[@id="__next"]/div/section[2]/div/div/div/div[1]/div[2]/span/span[1]/span')
click_drop.click()
click_form = driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
click_form.send_keys("Denmark")
click_form.send_keys(Keys.ENTER)

