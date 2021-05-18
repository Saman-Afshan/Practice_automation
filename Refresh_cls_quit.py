from selenium import webdriver

class Refresh():
    def ref(self):

        driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")
        url = "https://www.amazon.in/"
        driver.get(url)
        driver.refresh()   #refresh the page
        print("Did u noticed?__ Your page was Refreshed !!")
        #driver.close()
        driver.quit()



renew = Refresh()
renew.ref()





