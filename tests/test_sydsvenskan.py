import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


#CONSTANTS

SYDSVENSKAN = "https://www.sydsvenskan.se/"

#Tests

class TestClass:


    @pytest.fixture(scope="class")
    def load_driver(self):

        #options = Options()
        #options.headless = True
        driver = webdriver.Chrome()#(options=options)

        yield driver

        driver.quit()

    @pytest.fixture
    def get_sydsvenskan(self, load_driver):

        driver = load_driver

        #Loads website
        driver.get(SYDSVENSKAN)

        yield driver

        driver.delete_all_cookies()

    def test_title(self,get_sydsvenskan):
        driver = get_sydsvenskan
        title = "Sydsvenskan – Nyheter Dygnet Runt"
        assert title == driver.title

    def test_search_function_url(self,get_sydsvenskan):
        driver = get_sydsvenskan
        driver.find_element (By.ID, "didomi-notice-agree-button").click()
        driver.find_element (By.CSS_SELECTOR, ".icon-search").click()
        word = "gubbe"
        driver.find_element (By.ID, "search-input").send_keys(word + Keys.RETURN)
        assert word in driver.current_url
    def test_logga_in(self,get_sydsvenskan):
        driver = get_sydsvenskan
        item = driver.find_element (By.XPATH, '//*[@id="root-element"]/body/header/div[2]/div/a').text
        expected = "Logga in"
        assert expected == item
    def test_prenumera(self,get_sydsvenskan):
        driver = get_sydsvenskan
        prenumenera = driver.find_element (By.CLASS_NAME,"top-bar__text").text
        expected = "Prenumerera på Sydsvenskan"
        assert expected == prenumenera
    def test_just_nu(self,get_sydsvenskan):
        driver = get_sydsvenskan
        justnu = driver.find_element (By.XPATH, '//*[@id="main-content"]/div[1]/div/div/div/span').text
        expected = "Just nu"
        assert expected == justnu

