from selenium import webdriver
import unittest

class crt_Url(unittest.TestCase):
    def test_url(self):

        driver = webdriver.Chrome(executable_path="F:\\Python\\chromedriver.exe")
        url = "https://www.amazon.in/"
        driver.get(url)

        crnt_url = driver.current_url
        print("Current url of the page is:" + crnt_url)


# link = Test_Url()
# link.test_url()
 












