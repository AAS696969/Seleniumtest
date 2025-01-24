from time import sleep

from select import select
from selenium import webdriver
# from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

file = open('log.txt', 'w')

# driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
# option.add_experimental_option('detach', True)
option.add_argument("--headless")
driver = webdriver.Chrome(options=option)


# end of setup

# SC functions............

def set_up():
    driver.get('http://www.saucedemo.com/')
    driver.maximize_window()

# End of SC functions............

# Tests........................

def login():
    user_name = driver.find_element(By.XPATH,  '//input[@id="user-name"]')
    login1 = "standard_user"
    user_name.send_keys(login1)
    file.write("Success write login\n")

    password = driver.find_element(By.XPATH,  '//input[@id="password"]')
    user_pass = "secret_sauce"
    password.send_keys(user_pass)
    file.write("Success write password\n")

    login_button= driver.find_element(By.XPATH, '//input[@id="login-button"]' )
    login_button.click()
    file.write("Success click login\n")

def fake_login():
    user_name = driver.find_element(By.XPATH,  '//input[@id="user-name"]')
    login1 = "standard_user"
    user_name.send_keys(login1)
    file.write("Success write login\n")

    password = driver.find_element(By.XPATH,  '//input[@id="password"]')
    user_pass = "secret_sauce1"
    password.send_keys(user_pass)
    file.write("Success fake password\n")

    login_button= driver.find_element(By.XPATH, '//input[@id="login-button"]' )
    login_button.click()
    file.write("Success click login\n")

def test_login_redirect():
    correct_url = "https://www.saucedemo.com/inventory.html"
    get_url = driver.current_url

    assert correct_url == get_url, "test_login_redirect is Failed"
    file.write("test_login_redirect is OK\n")


def test_context_after_login_is_correct():
    correct_text = "Products"
    current_text = driver.find_element(By.XPATH,  '//*[@id="header_container"]/div[2]/span')

    assert correct_text == current_text.text, "test_context_after_login_is_correct is Failed"
    file.write("test_context_after_login_is_correct is OK\n")



# main

def sc_real_login():
    set_up()
    login()

    select = Select(driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select'))

    sleep(2)
    select.select_by_visible_text("Price (low to high)")

#.................

file.close()
driver.quit()