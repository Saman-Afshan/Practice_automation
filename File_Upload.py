from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class FileTransfer():
    def file(self):
        driver = webdriver.Chrome(executable_path="F:\\Selenium\\chromedriver1.exe")
        url = 'http://demo.guru99.com/test/upload/'
        driver.maximize_window()
        driver.get(url)

        # to upload a file
        Upload = driver.find_element_by_id("uploadfile_0")
        Upload.send_keys("F:\Selenium_Pyhton\pythonProject\main.py")  # give path of file u wanna uplaod

        driver.find_element(By.XPATH, "//input[@id='terms']").click()

        driver.find_element(By.XPATH, "//button[normalize-space()='Submit File']").click()

        # Download file
        # Download = driver.find_element_by_id("downloadButton")
        # Download.click()
        # time.sleep(2)
        # print("Yeah..also..File Downloaded successfully..!!")
        driver.quit()

fl = FileTransfer()
fl.file()
