from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class Locators():
    def loc(self):

        driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")
        url = "http://www.demo.iscripts.com/netmenus/mrml/cms"
        driver.get(url)
        time.sleep(2)

        #1-By id
        Username = driver.find_element(By.ID, "username")
        Username.send_keys("admin")
        time.sleep(2)

        #2-By-XPATH
        #Username = driver.find_element(By.XPATH, "//input[@id='username']")
        #Username.send_keys("admin")

        #3-By_NAME
        Password = driver.find_element(By.NAME, "password")
        Password.send_keys("admin")
        time.sleep(2)

        #4-by CSS SELECTOR
        Signin = driver.find_element(By.CSS_SELECTOR,"button[name='submit']")
        Signin.click()

        #5-By-Class_name
        #Signin = driver.find_element(By.CLASS_NAME, "login_btn")
        #Signin.click()

        #6 -By - LINK
        #link = driver.find_element(By.LINK_TEXT, "iScripts NetMenus")
        #link.click()

        #7 -By - PLINK
        #Link = driver.find_element(By.PARTIAL_LINK_TEXT,"iScripts.c")
        #Link.click()

        driver.quit()

Execute = Locators()
Execute.loc()










