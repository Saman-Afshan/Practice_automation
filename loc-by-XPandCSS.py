from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class Locators():
    def loc(self):
        driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")
        url = "http://www.demo.iscripts.com/netmenus/mrml/cms"
        driver.maximize_window()
        driver.get(url)

        time.sleep(2)

        #-By-XPATH
        Username = driver.find_element(By.XPATH, "//input[@id='username']")
        Username.send_keys("admin")

        Password = driver.find_element(By.XPATH, "//input[@id='inputPassword']")
        Password.send_keys("admin")

        #-by CSS SELECTOR
        Signin = driver.find_element(By.CSS_SELECTOR, "button[name='submit']")
        Signin.click()
        time.sleep(2)


Execute = Locators()
Execute.loc()
