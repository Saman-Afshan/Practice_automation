from selenium import webdriver
import time

class Scroll():
    def UpDown(self):

        driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")
        url = "https://www.amazon.com/"
        driver.maximize_window()
        driver.get(url)
        time.sleep(2)

        driver.execute_script("window.scrollBy(0,500)")      #scroll down
        time.sleep(2)
        print("You Scrolled down..!!")

        driver.execute_script("window.scrollBy(500,-500)")  # scroll down
        time.sleep(2)
        print("You Scrolled Up again...!!")


        #to scroll down and up completely(...below code.........)-----------------------------

        # to scroll bottom of page
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # time.sleep(2)

        #to scroll to top of page
        # driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        # time.sleep(2)

Scrll = Scroll()
Scrll.UpDown()










