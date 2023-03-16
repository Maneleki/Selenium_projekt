import pytest

from pages.result import SydsvenskanResult
from pages.search import SydsvenskanSearch


@pytest.mark.parametrize("words", ["kärlek"])
def test_search_sydsvenskan(browser, words):
    search_page = SydsvenskanSearch(browser)
    result_page = SydsvenskanResult(browser)

    # Loading the home page
    search_page.load()

    # Clicks on the search button
    search_page.open_search()

    # The search words are introduced
    search_page.search(words)

    # Check if the words search on the searh page
    assert words == result_page.search_input_value()
    assert words == result_page.title()


def test_section_sydsvenskan(browser):
    pass

