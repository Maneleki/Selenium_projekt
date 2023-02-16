from selenium.webdriver.common.by import By

class SydsvenskanResult:

    # LOCATORS

    RESULT_LINKS = (By.CLASS_NAME, "prose-title")
    SEARCH_INPUT = (By.ID, "search-input")

    # INITIALIZER

    def __init__(self, browser):
        self.browser = browser

    # INTERACTION METHODS

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_elements(*self.SEARCH_INPUT)
        value = search_input.get_attribute("value")
        return value

    def title(self):
        return self.browser.title


