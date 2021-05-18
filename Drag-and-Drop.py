from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class DD():
    def Dpdw(self):
        driver = webdriver.Chrome(executable_path="F:\\Python\\chromedriver.exe")
        url = "https://letskodeit.teachable.com/p/practice"
        driver.maximize_window()
        driver.get(url)  # hit the url

        option = driver.find_element_by_css_selector("#carselect")
        option.click()

        sel = Select(option)
        # sel.select_by_index(2)
        # sel.select_by_value("benz")
        sel.select_by_visible_text("Honda")
        time.sleep(1)
        option.click()

        print("All went well..!!")
        driver.close()

drpdwn = DD()
drpdwn.Dpdw()
