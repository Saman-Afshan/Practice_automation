from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class FileTransfer():
    def file(self):
        driver = webdriver.Chrome(executable_path="F:F:\\Python\\chromedriver.exe")
        url = "https://demoqa.com/upload-download"
        driver.maximize_window()
        driver.get(url)

        # Download file
        Download = driver.find_element(By.ID, "downloadButton")
        Download.click()
        time.sleep(3)
        print("Yeah..also..File Downloaded successfully..!!")
        driver.close()

fl = FileTransfer()
fl.file()
