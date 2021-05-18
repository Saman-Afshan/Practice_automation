from selenium import webdriver

class Source():
    def page(self):

        driver = webdriver.Chrome(executable_path="F:\\Selenium_Pyhton\\chromedriver.exe")
        url = "https://www.amazon.in/"
        driver.get(url)

        #get page source
        PageSource = driver.page_source
        print(PageSource)

        print("Huge code Above printed is your Page source!!")

YourSource = Source()
YourSource.page()





