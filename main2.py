from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

file = open("log.txt", "w")

driver = webdriver.Chrome()

def set_up():
    driver.get('http://www.saucedemo.com/')
    driver.maximize_window()

def login():
    user_name = driver.find_element(By.XPATH,  '//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)
    file.write("Success write login\n")

    password = driver.find_element(By.XPATH,  '//input[@id="password"]')
    user_pass = "secret_sauce"
    password.send_keys(user_pass)
    file.write("Success write password\n")

    sleep(2)

    login_button= driver.find_element(By.XPATH, '//input[@id="login-button"]' )
    login_button.click()
    file.write("Success click login\n")

set_up()
login()

sleep(5)
file.close()
driver.quit()