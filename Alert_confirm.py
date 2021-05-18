from selenium import webdriver
import time


class Alert:
    def alrt(self):
        driver = webdriver.Chrome(executable_path="F:\\Python\\chromedriver.exe")
        url = "https://letskodeit.teachable.com/p/practice"
        driver.maximize_window()
        driver.get(url)
        print("You hit the url")

        driver.find_element_by_id("name").send_keys("Python")
        driver.find_element_by_css_selector("#alertbtn").click()
        alert = driver.switch_to.alert
        time.sleep(0.9)
        alert.accept()
        print("Your alert was accepted")

        # driver.find_element_by_xpath("//input[@id='confirmbtn']").click()
        # confirm = driver.switch_to.alert
        # time.sleep()
        # confirm.dismiss()

popup = Alert()
popup.alrt()
