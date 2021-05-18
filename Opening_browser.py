
from selenium import webdriver

class title():
    def test(self):

        driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")
        url = "https://www.amazon.in/"
        driver.get(url)
        print("Hurray....Browser was opened!!")


heading = title()
heading.test()