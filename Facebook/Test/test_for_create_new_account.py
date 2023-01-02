from Facebook.Base_Test.locaterForCreateNewAccount import *
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_create_account_correct():
    driver = webdriver.Chrome()
    driver.get(facebook)
    sleep(2)
    driver.find_element(By.XPATH, create_btn).click()
    sleep(2)
    f_name = driver.find_element(By.XPATH, f_name_field)
    f_name.clear()
    f_name.send_keys("sam")
    sleep(2)
    l_name = driver.find_element(By.XPATH, l_name_field)
    l_name.clear()
    l_name.send_keys("wizz")
    sleep(2)
    phoneOrEmail = driver.find_element(By.XPATH, phone_or_email_field)
    phoneOrEmail.clear()
    phoneOrEmail.send_keys("0534635749")
    sleep(2)
    password = driver.find_element(By.XPATH, new_password_field)
    password.clear()
    password.send_keys("******")
    sleep(2)
    select_date = Select(driver.find_element(By.ID, day))
    select_date.select_by_visible_text("28")
    select_month = Select(driver.find_element(By.ID, month))
    select_month.select_by_visible_text("Apr")
    sleep(2)
    select_year = Select(driver.find_element(By.ID, year))
    select_year.select_by_visible_text("2000")
    sleep(2)
    driver.find_element(By.XPATH, gender_male).click()
    sleep(2)
    driver.find_element(By.XPATH, sign_up_button).click()
    sleep(5)
    driver.close()

def test_create_account_f_name_incorrect():
    driver = webdriver.Chrome()
    driver.get(facebook)
    sleep(2)
    driver.find_element(By.XPATH, create_btn).click()
    sleep(2)
    f_name = driver.find_element(By.XPATH, f_name_field)
    f_name.clear()
    f_name.send_keys("  ")
    l_name = driver.find_element(By.XPATH, l_name_field)
    l_name.clear()
    l_name.send_keys("wizz")
    phoneOrEmail = driver.find_element(By.XPATH, phone_or_email_field)
    phoneOrEmail.clear()
    phoneOrEmail.send_keys("0534635749")
    sleep(2)
    password = driver.find_element(By.XPATH, new_password_field)
    password.clear()
    password.send_keys("******")
    sleep(2)
    select_date = Select(driver.find_element(By.ID, day))
    select_date.select_by_visible_text("28")
    select_month = Select(driver.find_element(By.ID, month))
    select_month.select_by_visible_text("Apr")
    sleep(2)
    select_year = Select(driver.find_element(By.ID, year))
    select_year.select_by_visible_text("2000")
    sleep(2)
    driver.find_element(By.XPATH, gender_male).click()
    sleep(2)
    driver.find_element(By.XPATH, sign_up_button).click()
    sleep(5)
    error = driver.find_element(By.XPATH, error_text)
    assert error.is_enabled()
    driver.close()

def test_create_account_f_name_null():
    driver = webdriver.Chrome()
    driver.get(facebook)
    sleep(2)
    driver.find_element(By.XPATH, create_btn).click()
    sleep(2)
    f_name = driver.find_element(By.XPATH, f_name_field)
    f_name.clear()
    f_name.send_keys("")
    l_name = driver.find_element(By.XPATH, l_name_field)
    l_name.clear()
    l_name.send_keys("wizz")
    phoneOrEmail = driver.find_element(By.XPATH, phone_or_email_field)
    phoneOrEmail.clear()
    phoneOrEmail.send_keys("0534635749")
    sleep(2)
    password = driver.find_element(By.XPATH, new_password_field)
    password.clear()
    password.send_keys("******")
    sleep(2)
    select_date = Select(driver.find_element(By.ID, day))
    select_date.select_by_visible_text("28")
    select_month = Select(driver.find_element(By.ID, month))
    select_month.select_by_visible_text("Apr")
    sleep(2)
    select_year = Select(driver.find_element(By.ID, year))
    select_year.select_by_visible_text("2000")
    sleep(2)
    driver.find_element(By.XPATH, gender_male).click()
    sleep(2)
    driver.find_element(By.XPATH, sign_up_button).click()
    sleep(5)
    error = driver.find_element(By.XPATH, error_text)
    assert error.is_enabled()
    driver.close()

def test_create_account_l_name_incorrect():
    driver = webdriver.Chrome()
    driver.get(facebook)
    sleep(2)
    driver.find_element(By.XPATH, create_btn).click()
    sleep(2)
    f_name = driver.find_element(By.XPATH, f_name_field)
    f_name.clear()
    f_name.send_keys("sam")
    l_name = driver.find_element(By.XPATH, l_name_field)
    l_name.clear()
    l_name.send_keys("  ")
    phoneOrEmail = driver.find_element(By.XPATH, phone_or_email_field)
    phoneOrEmail.clear()
    phoneOrEmail.send_keys("0534635749")
    sleep(2)
    password = driver.find_element(By.XPATH, new_password_field)
    password.clear()
    password.send_keys("******")
    sleep(2)
    select_date = Select(driver.find_element(By.ID, day))
    select_date.select_by_visible_text("28")
    select_month = Select(driver.find_element(By.ID, month))
    select_month.select_by_visible_text("Apr")
    sleep(2)
    select_year = Select(driver.find_element(By.ID, year))
    select_year.select_by_visible_text("2000")
    sleep(2)
    driver.find_element(By.XPATH, gender_male).click()
    sleep(2)
    driver.find_element(By.XPATH, sign_up_button).click()
    sleep(5)
    driver.close()

def test_create_account_l_name_null():
    driver = webdriver.Chrome()
    driver.get(facebook)
    sleep(2)
    driver.find_element(By.XPATH, create_btn).click()
    sleep(2)
    f_name = driver.find_element(By.XPATH, f_name_field)
    f_name.clear()
    f_name.send_keys("sam")
    l_name = driver.find_element(By.XPATH, l_name_field)
    l_name.clear()
    l_name.send_keys("")
    phoneOrEmail = driver.find_element(By.XPATH, phone_or_email_field)
    phoneOrEmail.clear()
    phoneOrEmail.send_keys("0534635749")
    sleep(2)
    password = driver.find_element(By.XPATH, new_password_field)
    password.clear()
    password.send_keys("******")
    sleep(2)
    select_date = Select(driver.find_element(By.ID, day))
    select_date.select_by_visible_text("28")
    select_month = Select(driver.find_element(By.ID, month))
    select_month.select_by_visible_text("Apr")
    sleep(2)
    select_year = Select(driver.find_element(By.ID, year))
    select_year.select_by_visible_text("2000")
    sleep(2)
    driver.find_element(By.XPATH, gender_male).click()
    sleep(2)
    driver.find_element(By.XPATH, sign_up_button).click()
    sleep(5)
    driver.close()

def test_create_account_incorrect_phone_or_email():
    driver = webdriver.Chrome()
    driver.get(facebook)
    sleep(2)
    driver.find_element(By.XPATH, create_btn).click()
    sleep(2)
    f_name = driver.find_element(By.XPATH, f_name_field)
    f_name.clear()
    f_name.send_keys("sam")
    l_name = driver.find_element(By.XPATH, l_name_field)
    l_name.clear()
    l_name.send_keys("wizz")
    phoneOrEmail = driver.find_element(By.XPATH, phone_or_email_field)
    phoneOrEmail.clear()
    phoneOrEmail.send_keys("fhhhghh")
    sleep(2)
    password = driver.find_element(By.XPATH, new_password_field)
    password.clear()
    password.send_keys("******")
    sleep(2)
    select_date = Select(driver.find_element(By.ID, day))
    select_date.select_by_visible_text("28")
    select_month = Select(driver.find_element(By.ID, month))
    select_month.select_by_visible_text("Apr")
    sleep(2)
    select_year = Select(driver.find_element(By.ID, year))
    select_year.select_by_visible_text("2000")
    sleep(2)
    driver.find_element(By.XPATH, gender_male).click()
    sleep(2)
    driver.find_element(By.XPATH, sign_up_button).click()
    sleep(5)
    driver.close()

def test_create_account_null_phone_or_email():
    driver = webdriver.Chrome()
    driver.get(facebook)
    sleep(2)
    driver.find_element(By.XPATH, create_btn).click()
    sleep(2)
    f_name = driver.find_element(By.XPATH, f_name_field)
    f_name.clear()
    f_name.send_keys("sam")
    l_name = driver.find_element(By.XPATH, l_name_field)
    l_name.clear()
    l_name.send_keys("wizz")
    phoneOrEmail = driver.find_element(By.XPATH, phone_or_email_field)
    phoneOrEmail.clear()
    phoneOrEmail.send_keys("")
    sleep(2)
    password = driver.find_element(By.XPATH, new_password_field)
    password.clear()
    password.send_keys("******")
    sleep(2)
    select_date = Select(driver.find_element(By.ID, day))
    select_date.select_by_visible_text("28")
    select_month = Select(driver.find_element(By.ID, month))
    select_month.select_by_visible_text("Apr")
    sleep(2)
    select_year = Select(driver.find_element(By.ID, year))
    select_year.select_by_visible_text("2000")
    sleep(2)
    driver.find_element(By.XPATH, gender_male).click()
    sleep(2)
    driver.find_element(By.XPATH, sign_up_button).click()
    sleep(5)
    driver.close()

def test_create_account_incorrect_new_password():
    driver = webdriver.Chrome()
    driver.get(facebook)
    sleep(2)
    driver.find_element(By.XPATH, create_btn).click()
    sleep(2)
    f_name = driver.find_element(By.XPATH, f_name_field)
    f_name.clear()
    f_name.send_keys("sam")
    l_name = driver.find_element(By.XPATH, l_name_field)
    l_name.clear()
    l_name.send_keys("wizz")
    phoneOrEmail = driver.find_element(By.XPATH, phone_or_email_field)
    phoneOrEmail.clear()
    phoneOrEmail.send_keys("0534635749")
    sleep(2)
    password = driver.find_element(By.XPATH, new_password_field)
    password.clear()
    password.send_keys("/")
    sleep(2)
    select_date = Select(driver.find_element(By.ID, day))
    select_date.select_by_visible_text("28")
    select_month = Select(driver.find_element(By.ID, month))
    select_month.select_by_visible_text("Apr")
    sleep(2)
    select_year = Select(driver.find_element(By.ID, year))
    select_year.select_by_visible_text("2000")
    sleep(2)
    driver.find_element(By.XPATH, gender_male).click()
    sleep(2)
    driver.find_element(By.XPATH, sign_up_button).click()
    sleep(5)
    driver.close()

def test_create_account_incorrect_f_name_and_lname():
    driver = webdriver.Chrome()
    driver.get(facebook)
    sleep(2)
    driver.find_element(By.XPATH, create_btn).click()
    sleep(2)
    f_name = driver.find_element(By.XPATH, f_name_field)
    f_name.clear()
    f_name.send_keys(" ")
    l_name = driver.find_element(By.XPATH, l_name_field)
    l_name.clear()
    l_name.send_keys("  ")
    phoneOrEmail = driver.find_element(By.XPATH, phone_or_email_field)
    phoneOrEmail.clear()
    phoneOrEmail.send_keys("0534635749")
    sleep(2)
    password = driver.find_element(By.XPATH, new_password_field)
    password.clear()
    password.send_keys("******")
    sleep(2)
    select_date = Select(driver.find_element(By.ID, day))
    select_date.select_by_visible_text("28")
    select_month = Select(driver.find_element(By.ID, month))
    select_month.select_by_visible_text("Apr")
    sleep(2)
    select_year = Select(driver.find_element(By.ID, year))
    select_year.select_by_visible_text("2000")
    sleep(2)
    driver.find_element(By.XPATH, gender_male).click()
    sleep(2)
    driver.find_element(By.XPATH, sign_up_button).click()
    sleep(5)
    error = driver.find_element(By.XPATH, error_text)
    assert error.is_enabled()
    driver.close()

def test_create_account_incorrect_f_name_and_lname_and_phone():
    driver = webdriver.Chrome()
    driver.get(facebook)
    sleep(2)
    driver.find_element(By.XPATH, create_btn).click()
    sleep(3)
    f_name = driver.find_element(By.XPATH, f_name_field)
    f_name.clear()
    f_name.send_keys(" ")
    sleep(2)
    l_name = driver.find_element(By.XPATH, l_name_field)
    l_name.clear()
    l_name.send_keys("  ")
    sleep(2)
    phoneOrEmail = driver.find_element(By.XPATH, phone_or_email_field)
    phoneOrEmail.clear()
    phoneOrEmail.send_keys("0534")
    sleep(2)
    password = driver.find_element(By.XPATH, new_password_field)
    password.clear()
    password.send_keys("******")
    sleep(2)
    select_date = Select(driver.find_element(By.ID, day))
    select_date.select_by_visible_text("28")
    select_month = Select(driver.find_element(By.ID, month))
    select_month.select_by_visible_text("Apr")
    sleep(2)
    select_year = Select(driver.find_element(By.ID, year))
    select_year.select_by_visible_text("2000")
    sleep(2)
    driver.find_element(By.XPATH, gender_femail).click()
    sleep(2)
    driver.find_element(By.XPATH, sign_up_button).click()
    sleep(5)
    error = driver.find_element(By.XPATH, error_text)
    assert error.is_enabled()
    driver.close()

def test_create_account_incorrect():
    driver = webdriver.Chrome()
    driver.get(facebook)
    sleep(2)
    driver.find_element(By.XPATH, create_btn).click()
    sleep(3)
    f_name = driver.find_element(By.XPATH, f_name_field)
    f_name.clear()
    f_name.send_keys(" ")
    sleep(2)
    l_name = driver.find_element(By.XPATH, l_name_field)
    l_name.clear()
    l_name.send_keys("  ")
    sleep(2)
    phoneOrEmail = driver.find_element(By.XPATH, phone_or_email_field)
    phoneOrEmail.clear()
    phoneOrEmail.send_keys("0534")
    sleep(2)
    password = driver.find_element(By.XPATH, new_password_field)
    password.clear()
    password.send_keys("***")
    sleep(2)
    select_date = Select(driver.find_element(By.ID, day))
    select_date.select_by_visible_text("1")
    select_month = Select(driver.find_element(By.ID, month))
    select_month.select_by_visible_text("Jan")
    sleep(2)
    select_year = Select(driver.find_element(By.ID, year))
    select_year.select_by_visible_text("2023")
    sleep(2)
    driver.find_element(By.XPATH, gender_femail).click()
    sleep(2)
    driver.find_element(By.XPATH, sign_up_button).click()
    sleep(5)
    error = driver.find_element(By.XPATH, error_text)
    assert error.is_enabled()
    driver.close()

def test_create_account_all_null():
    driver = webdriver.Chrome()
    driver.get(facebook)
    sleep(2)
    driver.find_element(By.XPATH, create_btn).click()
    sleep(3)
    f_name = driver.find_element(By.XPATH, f_name_field)
    f_name.clear()
    f_name.send_keys("")
    sleep(2)
    l_name = driver.find_element(By.XPATH, l_name_field)
    l_name.clear()
    l_name.send_keys("")
    sleep(2)
    phoneOrEmail = driver.find_element(By.XPATH, phone_or_email_field)
    phoneOrEmail.clear()
    phoneOrEmail.send_keys("")
    sleep(2)
    password = driver.find_element(By.XPATH, new_password_field)
    password.clear()
    password.send_keys("")
    sleep(2)
    select_date = Select(driver.find_element(By.ID, day))
    select_date.select_by_visible_text("1")
    select_month = Select(driver.find_element(By.ID, month))
    select_month.select_by_visible_text("Jan")
    sleep(2)
    select_year = Select(driver.find_element(By.ID, year))
    select_year.select_by_visible_text("2023")
    sleep(2)
    # driver.find_element(By.XPATH, custom).click()
    sleep(2)
    driver.find_element(By.XPATH, sign_up_button).click()
    sleep(5)
    error = driver.find_element(By.XPATH, error_text)
    assert error.is_enabled()
    driver.close()



