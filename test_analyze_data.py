import pytest
import pandas as pd
from bs4 import BeautifulSoup as bs

from get_data import (
    get_price_and_peak,
    get_name,
    get_reviews,
    get_game_genre,
)

df = pd.read_csv("steam_data.csv")

# Define sets of test cases.

get_price_and_peak_cases = [
    # Check that a game that is free has a price of 0
    (df.loc[0].at["Price"], 0.0),
    # Check a game with a price under 10
    (df.loc[17].at["Price"], 3.99),
    # Check a game with a price under 20
    (df.loc[4].at["Price"], 14.99),
    # Check a game with a price under 30
    (df.loc[27].at["Price"], 29.99),
    # Check a game with a price under 40
    (df.loc[10].at["Price"], 39.99),
    # Check a game with a price under 50
    (df.loc[22].at["Price"], 44.99),
    # Check a game with a price above 50
    (df.loc[36].at["Price"], 59.99),
]

get_name_cases = []

get_reviews_cases = []

get_game_genre_cases = []


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("price", get_price_and_peak_cases)
def test_get_tbody(price, peak, price_exp, peak_exp):
    """
    Test that the price and peak data in the csv file (acquired from
    running get_price_and_peak) is the expected result.

    Args:
        price: The price in the csv file
        peak: The peak number of players in the csv file
        price_exp: A string representing the expected price
        peak_exp: A string representing the expected peak players
    """
    assert isinstance(price, str, peak, str)
    assert price_exp == price
    assert peak_exp == peak


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
