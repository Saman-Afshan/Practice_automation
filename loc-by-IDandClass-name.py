from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class Locators():
    def loc(self):

        driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")
        url = "http://www.demo.iscripts.com/netmenus/mrml/cms"
        driver.get(url)
        time.sleep(2)

        #By_Id

        Username = driver.find_element(By.ID, "username")
        Username.send_keys("admin")

        Password = driver.find_element(By.NAME, "password")
        Password.send_keys("admin")
        time.sleep(2)

        #BY_Class-Name

        Signin = driver.find_element(By.CLASS_NAME, "login_btn")
        Signin.click()
        time.sleep(2)


Execute = Locators()
Execute.loc()
