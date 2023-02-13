from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException


try:
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    driver.find_element(By.ID, "email").send_keys(
        "fakeemail@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("dummypass")
    driver.find_element(By.NAME, "login").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//input[@aria-label='Buscar en Facebook']")))
    print("good")
except NoSuchElementException:  # spelling error making this code not work as expected
    raise Exception("Elements can´t be found")
except TimeoutException:  # spelling error making this code not work as expected
    raise Exception("Error de Timeout")
