from selenium import webdriver
import time
from selenium.webdriver import ActionChains

class MouseHover():
    def mshvr(self):
        driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")
        url = "https://www.amazon.com/"
        driver.maximize_window()
        driver.get(url)   # hit the url

        action = driver.find_element_by_css_selector("span[class='icp-nav-flag icp-nav-flag-us']")  # hovers on flag
        act_chain = ActionChains(driver)
        act_chain.move_to_element(action).perform()
        time.sleep(2)
        print("Did u watch that...Mouse hover works well...!!")



yourclick = MouseHover()
yourclick.mshvr()
