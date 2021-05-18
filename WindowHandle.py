from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")
url = ""
driver.get(url)
driver.maximize_window()

main = driver.find_element(By.)
driver.title