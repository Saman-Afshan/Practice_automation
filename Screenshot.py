from selenium import webdriver

class Screenshot:
    def scrnsht(self):
        driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")
        url = "https://www.amazon.com/"
        driver.maximize_window()
        driver.get(url)

        # to take screenshot
        driver.get_screenshot_as_file("Autoshot.png")   # give file name u want to save ur scrnshot as!
        print("Captured Successfully...!! ")
        print("You can check ur file...")

        # also different path with file name can be given wherever u want to store ur image..
        # driver.get_screenshot_as_file("F:\Selenium_Pyhton\Autoshot.png")


pic = Screenshot()
pic.scrnsht()
