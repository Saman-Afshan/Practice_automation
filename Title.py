from selenium import webdriver


class title():
    def test(self):
        driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")
        url = "https://www.amazon.in/"
        driver.get(url)

        titl = driver.title
        print("Title of the web page is: " + titl)
        # print(driver.title)


heading = title()
heading.test()
