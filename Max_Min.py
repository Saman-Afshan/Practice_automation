from selenium import webdriver
import time

class MaxMin():
    def Size(self):

        driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")
        url = "https://www.amazon.in/"
        driver.maximize_window()
        driver.get(url)

        print("Window Maximized Done!!")
        driver.minimize_window()
        time.sleep(5)
        print("Window Minimize Done!! ")



mm = MaxMin()
mm.Size()




