from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ATID_Demo_Store.Base_Test.locater import *


def test_store_buy_product():

    driver = webdriver.Chrome()
    driver.get("https://atid.store/")
    driver.find_element(By.XPATH, store).click()
    sleep(2)
    driver.find_element(By.XPATH, Green_Tshirt).click()
    sleep(2)
    driver.find_element(By.XPATH,add_cart_btn).click()
    sleep(2)
    driver.find_element(By.XPATH,cart_btn).click()
    sleep(2)
    product_name = driver.find_element(By.XPATH, path_of_Green_Tshirt).text
    assert product_name == 'ATID Green Tshirt'

def test_men_buy_product():
    driver = webdriver.Chrome()
    driver.get("https://atid.store/")
    driver.find_element(By.XPATH, MEN).click()
    sleep(2)
    driver.find_element(By.XPATH, Dark_Blue_Denim_Jeans).click()
    sleep(2)
    driver.find_element(By.XPATH, add_cart_btn).click()
    sleep(2)
    driver.find_element(By.XPATH,cart_btn).click()
    sleep(2)
    product_name = driver.find_element(By.XPATH, path_of_Dark_Blue_Denim_Jeans).text
    assert product_name == 'Dark Blue Denim Jeans'

def test_women_buy_product():
    driver = webdriver.Chrome()
    driver.get("https://atid.store/")
    driver.find_element(By.XPATH, WOMEN).click()
    sleep(2)
    driver.find_element(By.XPATH, Bright_Gold_Purse_With_Chain).click()
    sleep(2)
    driver.find_element(By.XPATH, add_cart_btn).click()
    sleep(2)
    driver.find_element(By.XPATH,cart_btn).click()
    sleep(2)
    product_name = driver.find_element(By.XPATH, path_of_Bright_Gold_Purse_With_Chain).text
    assert product_name == 'Bright Gold Purse With Chain'

def test_accessories_buy_product():
    driver = webdriver.Chrome()
    driver.get("https://atid.store/")
    driver.find_element(By.XPATH, ACCESSORIES).click()
    sleep(2)
    driver.find_element(By.XPATH, Boho_Bangle_Bracelet).click()
    sleep(2)
    driver.find_element(By.XPATH, add_cart_btn).click()
    sleep(2)
    driver.find_element(By.XPATH, cart_btn).click()
    sleep(2)
    product_name = driver.find_element(By.XPATH, path_of_Boho_Bangle_Bracelet).text
    assert product_name == 'Boho Bangle Bracelet'


def test_for_coupon():
    driver = webdriver.Chrome()
    driver.get("https://atid.store/")
    driver.find_element(By.XPATH, ACCESSORIES).click()
    sleep(2)
    driver.find_element(By.XPATH, Boho_Bangle_Bracelet).click()
    sleep(2)
    driver.find_element(By.XPATH, add_cart_btn).click()
    sleep(2)
    driver.find_element(By.XPATH, cart_btn).click()
    sleep(2)
    product_name = driver.find_element(By.XPATH, path_of_Boho_Bangle_Bracelet).text
    assert product_name == 'Boho Bangle Bracelet'
    coupon = driver.find_element(By.XPATH, coupon_field)
    sleep(2)
    coupon.clear()
    coupon.send_keys("abc123")
    sleep(2)
    driver.find_element(By.XPATH, apply_btn).click()
    sleep(2)
    j = driver.find_element(By.XPATH, pathOfResponseText).text

    assert j == "Please enter a coupon code."
    sleep(2)
