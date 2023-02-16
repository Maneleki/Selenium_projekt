
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SydsvenskanSearch:

    # URL

    URL = "https://sydsvenskan.se"

    #LOCATORS

    SEARCH_INPUT = (By.ID, "search-input")

    # INITIALIZER

    def __init__(self, browser):
        self.browser = browser

    # INTERACTION METHODS

    def load(self):
        self.browser.get(self.URL)

    def open_search(self):
        search_button = (By.CSS_SELECTOR, "icon-search")
        search_button.click()

    def search(self, words):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(words + Keys.RETURN)