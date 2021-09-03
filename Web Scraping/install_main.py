from selenium import webdriver

chrome_driver = "C:\Chrome Driver/chromedriver"

driver = webdriver.Chrome(chrome_driver)
driver.get('https://www.google.com')