from Facebook.Base_Test.locaterForLogin import *

from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def test_login_correct():
    driver = webdriver.Chrome()
    driver.get(facebook)
    assert "Facebook – log in or sign up" in driver.title
    phone = driver.find_element(By.XPATH, emailOrPhoneNumberField)
    # phone.clear()
    phone.send_keys("0534635749")
    sleep(2)
    password = driver.find_element(By.ID, passwordField)
    password.send_keys("******")
    sleep(2)
    driver.find_element(By.NAME, login_button).click()
    sleep(30)

def test_login_incorrect_phone():
    driver = webdriver.Chrome()
    driver.get(facebook)
    # sleep(3)
    assert "Facebook – log in or sign up" in driver.title
    phone = driver.find_element(By.XPATH, emailOrPhoneNumberField)
    phone.clear()
    phone.send_keys("0534635712")
    sleep(2)
    password = driver.find_element(By.ID, passwordField)
    password.send_keys("******")
    sleep(2)
    driver.find_element(By.NAME, login_button).click()
    sleep(5)


def test_login_incorrect_password():
    driver = webdriver.Chrome()
    driver.get(facebook)
    # sleep(3)
    assert "Facebook – log in or sign up" in driver.title
    phone = driver.find_element(By.XPATH, emailOrPhoneNumberField)
    phone.clear()
    phone.send_keys("0534635749")
    sleep(2)
    password = driver.find_element(By.ID, passwordField)
    password.send_keys("125463")
    sleep(2)
    driver.find_element(By.NAME, login_button).click()
    sleep(5)

def test_login_incorrect_password_and_phone():
    driver = webdriver.Chrome()
    driver.get(facebook)
    # sleep(3)
    assert "Facebook – log in or sign up" in driver.title
    phone = driver.find_element(By.XPATH, emailOrPhoneNumberField)
    phone.clear()
    phone.send_keys("0534635712")
    sleep(2)
    password = driver.find_element(By.ID, passwordField)
    password.send_keys("125463")
    sleep(2)
    driver.find_element(By.NAME, login_button).click()
    sleep(5)

def test_login_null_phone_and_correct_password():
    driver = webdriver.Chrome()
    driver.get(facebook)
    # sleep(3)
    assert "Facebook – log in or sign up" in driver.title
    phone = driver.find_element(By.XPATH, emailOrPhoneNumberField)
    phone.clear()
    phone.send_keys("")
    sleep(2)
    password = driver.find_element(By.ID, passwordField)
    password.send_keys("******")
    sleep(2)
    driver.find_element(By.NAME, login_button).click()
    sleep(5)

def test_login_null_password_and_correct_phone():
    driver = webdriver.Chrome()
    driver.get(facebook)
    # sleep(3)
    assert "Facebook – log in or sign up" in driver.title
    phone = driver.find_element(By.XPATH, emailOrPhoneNumberField)
    phone.clear()
    phone.send_keys("0534635749")
    sleep(2)
    password = driver.find_element(By.ID, passwordField)
    password.send_keys("")
    sleep(2)
    driver.find_element(By.NAME, login_button).click()
    sleep(5)

def test_login_null_password_and_incorrect_phone():
    driver = webdriver.Chrome()
    driver.get(facebook)
    # sleep(3)
    assert "Facebook – log in or sign up" in driver.title
    phone = driver.find_element(By.XPATH, emailOrPhoneNumberField)
    phone.clear()
    phone.send_keys("0534635712")
    sleep(2)
    password = driver.find_element(By.ID, passwordField)
    password.send_keys("")
    sleep(2)
    driver.find_element(By.NAME, login_button).click()
    sleep(5)

def test_login_null_phone_and_incorrect_password():
    driver = webdriver.Chrome()
    driver.get(facebook)
    # sleep(3)
    assert "Facebook – log in or sign up" in driver.title
    phone = driver.find_element(By.XPATH, emailOrPhoneNumberField)
    phone.clear()
    phone.send_keys("")
    sleep(2)
    password = driver.find_element(By.ID, passwordField)
    password.send_keys("123546")
    sleep(2)
    driver.find_element(By.NAME, login_button).click()
    sleep(5)

def test_login_password_and_phone_null():
    driver = webdriver.Chrome()
    driver.get(facebook)
    # sleep(3)
    assert "Facebook – log in or sign up" in driver.title
    phone = driver.find_element(By.XPATH, emailOrPhoneNumberField)
    phone.clear()
    phone.send_keys("")
    sleep(2)
    password = driver.find_element(By.ID, passwordField)
    password.send_keys("")
    sleep(2)
    driver.find_element(By.NAME, login_button).click()
    sleep(5)