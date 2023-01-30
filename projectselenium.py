from selenium import webdriver
import time

PATH = "C:\Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://sydsvenskan.se")
print(driver.title)
driver.quit()

