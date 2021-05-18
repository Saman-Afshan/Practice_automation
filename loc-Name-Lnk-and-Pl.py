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

        #By-Name
        Username = driver.find_element(By.NAME, "username")
        Username.send_keys("admin")

        driver.find_element_by_name("password").send_keys("admin12")
        print("Entered Wrong password !!")
        time.sleep(1)
        driver.find_element_by_name("password").clear()
        time.sleep(1)


        #By-Link
        link = driver.find_element(By.LINK_TEXT, "iScripts NetMenus")
        link.click()
        time.sleep(1)

        #By-Partial-link
        Link = driver.find_element(By.PARTIAL_LINK_TEXT,"iScripts.c")
        Link.click()
        time.sleep(2)

Execute = Locators()
Execute.loc()