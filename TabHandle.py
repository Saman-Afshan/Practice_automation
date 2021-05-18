from selenium import webdriver
from selenium.webdriver.common.by import By

class HandleFrames():
    def hfrm(self):
        driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")
        url = "https://demoqa.com/frames"
        driver.maximize_window()
        driver.get(url)  # hit the url

        # switch to first frame
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='frame1']"))
        header_1 = driver.find_element_by_tag_name("h1").text
        print("You switched to first frame..!!")
        print(header_1)

        # switch back to default content
        driver.switch_to.default_content()
        print("You switched back to default content..!!")

        # switch to second frame
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='frame2']"))
        header_2 = driver.find_element(By.CSS_SELECTOR, "#sampleHeading").text
        print("You switched to second frame...!!")
        print(header_2)


        driver.quit()

hf= HandleFrames()
hf.hfrm()
