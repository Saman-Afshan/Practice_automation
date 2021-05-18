from selenium import webdriver
import time

class Alert:
    def alrt(self):
        driver = webdriver.Chrome(executable_path="F:\\Python\\chromedriver.exe")
        url = "https://letskodeit.teachable.com/p/practice"
        driver.maximize_window()
        driver.get(url)                  # you hit the url

        text = "I am Alert box.....Cancel me!!"
        driver.find_element_by_id("name").send_keys(text)

        driver.find_element_by_xpath("//input[@id='confirmbtn']").click()

        cancel = driver.switch_to.alert
        time.sleep(0.9)
        cancel.dismiss()
        print("Alert was cancel")

popup = Alert()
popup.alrt()