from selenium import webdriver

class Navigate():
    def fandb(self):

        driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")
        url = "https://www.google.com/"
        driver.get(url)

        another_url = "https://www.amazon.in/"
        driver.get(another_url)

        driver.back()
        print("You were back to previous url!!")
        driver.forward()
        print("You moved forward to next url agian!! ")



nav = Navigate()
nav.fandb()