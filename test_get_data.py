"""
This module runs unit test
"""

import pytest
import pandas as pd
from bs4 import BeautifulSoup

from get_data import get_game_links, get_name, get_price_and_peak

df = pd.read_csv("steam_data.csv")

# Define sets of test cases.


get_game_links_cases = [
    # Check that an empty tbody returns no links
    ("", []),
    # Check that a tbody with one link returns that link
    (
        "https://store.steampowered.com/app/730/CounterStrike_2?",
        ["https://store.steampowered.com/app/730/CounterStrike_2?"],
    ),
    # Check that a tbody with one link and other info only returns the link
    (
        "hello-https://store.steampowered.com/app/730/CounterStrike_2?-goodbye",
        ["https://store.steampowered.com/app/730/CounterStrike_2?"],
    ),
    # Check that a tbody with multiple links returns all links
    (
        (
            "hello-https://store.steampowered.com/app/730/CounterStrike_2?-good"
            "bye-https://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS?-"
            "bye"
        ),
        [
            "https://store.steampowered.com/app/730/CounterStrike_2?",
            "https://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS?",
        ],
    ),
]

get_names_cases = [
    # Check that a link returns the correct name
    (
        "https://store.steampowered.com/app/730/CounterStrike_2?",
        "CounterStrike_2",
    ),
]

get_price_and_peak_cases = [
    # Check that a game that is free has a price of 0
    # Check that peak players gets returned properly
    ("<tr hello>Free to Play</tr>", 0.0),
    # Check a game with a numbered price and tbody with
    # other stuff returns properly
]

get_reviews_cases = []


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("tbody,link_exp", get_game_links_cases)
def test_get_game_links(tbody, link_exp):
    """
    Test that game links are successfully retrieved from the website.

    Args:
        tbody: A string representing the text body of the HTML.
        link_exp: A list of strings representing the expected output
        game links.
    """
    assert isinstance(link_exp, list)
    for link in link_exp:
        assert isinstance(link, str)

    link = get_game_links(tbody)
    assert link == link_exp


@pytest.mark.parametrize("link,name_exp", get_names_cases)
def test_get_name(link, name_exp):
    """
    Test that a game name is successfully retrieved from the link.

    Args:
        link: A string representing the link to a game.
        name_exp: A string representing the expected output name.
    """
    name = get_name(link)
    assert isinstance(name, str)
    assert name == name_exp


@pytest.mark.parametrize(
    "game_name,price_exp,peak_exp", get_price_and_peak_cases
)
def test_get_price_and_peak(game_name, price_exp, peak_exp):
    """
    Test that the price and peak data in the csv file (acquired from
    running get_price_and_peak) is the expected result.

    Args:
        tbody: A string representing the HTML body text
        price_exp: A float representing the expected price
        peak_exp: An int representing the expected peak players
    """
    row_index = df.index[df["Game Name"] == game_name].tolist()[0]
    price_result = df.loc[row_index]["Price"]
    # Test that each are the correct data type, peak is changing every 24 hours
    # so we can't check expected peak value
    assert price_result == price_exp


def test_get_reviews():
    """
    Test that the game reviews and percentage of positivity
    are ints in the csv file.
    """
    # Only check that they are ints since reviews change
    # over time
    for review in df["Number of Reviews"]:
        assert isinstance(review, str)
    for percent in df["Percent Positive Reviews"]:
        assert isinstance(percent, int)


def test_get_game_genre():
    """
    Test that the game genres are all strings in
    the csv file
    """
    # Only check that they are strs since order
    # changes over time
    for genre1 in df["First Genre"]:
        assert isinstance(genre1, str)
    for genre2 in df["Second Genre"]:
        assert isinstance(genre2, str)
    for genre3 in df["Third Genre"]:
        assert isinstance(genre3, str)
