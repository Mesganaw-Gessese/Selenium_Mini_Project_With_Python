from Facebook.Base_Test.locaterForForgerPassword import *
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_forget_password_correct_phone():
    driver = webdriver.Chrome()
    driver.get(facebook)
    sleep(3)
    assert "Facebook – log in or sign up" in driver.title
    driver.find_element(By.XPATH, forgot_password_location).click()
    phone = driver.find_element(By.ID, fild)
    phone.clear()
    phone.send_keys("0534635749")
    sleep(2)
    driver.find_element(By.NAME, search_btn).click()
    sleep(5)
    reset = driver.find_element(By.XPATH, reset_password).text
    assert reset == "Reset your password"
    # assert "Password" in reset
    sleep(10)

def test_forget_password_incorrect_phone():
    driver = webdriver.Chrome()
    driver.get(facebook)
    sleep(3)
    assert "Facebook – log in or sign up" in driver.title
    driver.find_element(By.XPATH, forgot_password_location).click()
    phone = driver.find_element(By.ID, fild)
    phone.clear()
    phone.send_keys("0534635712")
    sleep(2)
    driver.find_element(By.NAME, search_btn).click()
    sleep(5)
    search_result = driver.find_element(By.XPATH, forgot_password_error_message).text
    assert search_result == "No search results"
    # assert "Password" in reset
    sleep(10)

def test_forget_password_null_phone():
    driver = webdriver.Chrome()
    driver.get(facebook)
    sleep(3)
    x = driver.title
    assert "Facebook – log in or sign up" in x
    driver.find_element(By.XPATH, forgot_password_location).click()
    phone = driver.find_element(By.ID, fild)
    phone.clear()
    phone.send_keys("")
    sleep(2)
    driver.find_element(By.NAME, search_btn).click()
    sleep(10)
    search_result = driver.find_element(By.XPATH, forgot_password_error_message).text

    assert search_result == "Please fill in at least one field"
    # assert "Password" in reset
    sleep(10)

