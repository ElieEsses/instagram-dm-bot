from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
# opens chrome

def initialize_insta(personal_user, personal_pass, target_username):
    driver.get('https://www.instagram.com/'+target_username)
    time.sleep(2)

    # finds and fills in username and password
    username_input = driver.find_element_by_css_selector("input[name='username']")
    username_input.send_keys(personal_user)
    password_input = driver.find_element_by_css_selector("input[name='password']")
    password_input.send_keys(personal_pass)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5.5)

    # finds and clicks Not Now button
    not_now = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Not Now"]')))
    not_now.click()

def send_dm(message):
    # finds and clicks Message button
    msg_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Message')]")))
    msg_button.click()
    time.sleep(3)

    # finds and clicks Not Now button again
    not_now2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Not Now"]')))
    not_now2.click()
    time.sleep(1)

    # sends message
    message_input = driver.find_element_by_css_selector("textarea[placeholder='Message...']")
    message_input.send_keys(message)
    message_input.send_keys(Keys.RETURN)
    time.sleep(.5)
