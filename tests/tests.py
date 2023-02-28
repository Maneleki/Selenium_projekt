import pytest

from pages.result import SydsvenskanResult
from pages.search import SydsvenskanSearch


@pytest.mark.parametrize("words", ["kärlek"])
def