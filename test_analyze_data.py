import pytest
import pandas as pd
from bs4 import BeautifulSoup as bs

from get_data import (
    get_tbody,
    get_game_links,
    get_price_and_peak,
    get_name,
    get_reviews,
    get_game_genre,
)

soup_test_data_list = [
    bs("<div></div>", "html.parser"),
    bs("<tbody>test</tbody>", "html.parser"),
]

# Define sets of test cases.
get_tbody_cases = [
    # Check html with no tbody
    (soup_test_data_list[0], ""),
    # Check html containing only tbody
    (soup_test_data_list[1], "test"),
]

get_game_links_cases = []

get_price_and_peak_cases = []

get_name_cases = []

get_reviews_cases = []

get_game_genre_cases = []


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("soup,tbody", get_tbody)
def test_get_tbody(soup, tbody):
    """
    Test that retrieving the body text from a beautiful soup object
    returns the correct result of what is between <tbody> and </tbody>

    Args:
        soup: A beautiful soup object of test html data
        tbody: A string of the expected results of the function
    """
    result = get_tbody(soup)
    assert isinstance(result, str)
    assert result == tbody


@pytest.mark.parametrize("tbody,links", get_game_links)
def test_get_game_links(tbody, links):
    """
    Test that retrieving the link from the tbody correctly returns
    the expected a string of a link.

    Args:
        tbody: A string extracted from html data
        links: A list of strings of the expected results of the
        function
    """
    result = get_game_links(tbody)
    assert isinstance(result, list)
    assert result == links


@pytest.mark.parametrize("tbody,price,peak", get_price_and_peak)
def test_get_price_and_peak(tbody, price, peak):
    """
    Test that extracting the price and peak players from the tbody
    returns the correct two integer values.

    Args:
        tbody: A string extracted from html data
        price: An int of the expected result of the function
        peak: An int of the second expected result of the function
    """
    result = get_price_and_peak(tbody)
    assert isinstance(result, int, int)
    assert result == price, peak
