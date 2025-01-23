from argparse import Action
from selenium import webdriver
from time import sleep
import time
from datetime import datetime, date, time, timedelta

from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# file = open("lognew.txt", "w")

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument("--headless")
driver = webdriver.Chrome(options=option)

driver.get("https://demoqa.com/date-picker")
driver.maximize_window()
sleep(1)

date_input = driver.find_element(By.XPATH, '//*[@id="datePickerMonthYearInput"]')
date_input.send_keys(Keys.CONTROL + "A")
date_input.send_keys(Keys.DELETE)
sleep(2)

today = date.today()
print(today)
future = str(today + timedelta(days = 10))
print(future)
date_input.send_keys(future)

# file.close()
