from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox()
LOGIN_BUTTON = (By.XPATH, '//*[@aria-label="Войти"]')
EMAIL_FIELD = (By.XPATH, '//*[@type="email"]')
NEXT_BUTTON = (By.XPATH, '//*[@id="identifierNext"]')
ERROR_TEXT = (By.XPATH, '//*[text()="Не удалось найти аккаунт Google."]')

def find_element(driver, locator, time=5):
    return WebDriverWait(driver, time).until(expected_conditions.presence_of_element_located(locator))

def test_error_auth():
    driver.get('https://www.google.ru')
    find_element(driver, LOGIN_BUTTON).click()
    find_element(driver, EMAIL_FIELD).send_keys("GGG")
    find_element(driver, NEXT_BUTTON).click()
    find_element(driver, ERROR_TEXT)


