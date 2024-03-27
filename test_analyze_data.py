import pytest
import pandas as pd

df = pd.read_csv("steam_data.csv")

# Define sets of test cases.

get_price_and_peak_cases = [
    # Check that a game that is free has a price of 0
    ("CounterStrike_2", 0.0),
    # Check a game with a price under 10
    ("Wallpaper_Engine", 3.99),
    # Check a game with a price under 20
    ("Stardew_Valley", 14.99),
    # Check a game with a price under 30
    ("Palworld", 29.99),
    # Check a game with a price under 40
    ("HELLDIVERS_2", 39.99),
    # Check a game with a price under 50
    ("Baldurs_Gate_3", 44.99),
    # Check a game with a price above 50
    ("Red_Dead_Redemption_2", 59.99),
]


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("game_name,price_exp", get_price_and_peak_cases)
def test_get_tbody(game_name, price_exp):
    """
    Test that the price and peak data in the csv file (acquired from
    running get_price_and_peak) is the expected result.

    Args:
        game_name: A string representing the name of a game
        price_exp: A float representing the expected price
        peak_exp: An int representing the expected peak players
    """
    price_result = df[df["Game Name"] == game_name].at["Price"]
    peak_result = df[df["Game Name"] == game_name].at["Peak Number of Players"]

    # Test that each are the correct data type, peak is changing every 24 hours
    # so we can't check expected peak value
    assert isinstance(price_result, float, peak_result, int)
    assert price_result == price_exp


def test_get_name():
    """
    Test that the game names are strings in the csv file.
    """
    # Only check that it is a string since order may change
    # over time
    for name in df["Game Name"]:
        assert isinstance(name, str)


def test_get_reviews():
    """
    Test that the game reviews and percentage of positivity
    are ints in the csv file.
    """
    # Only check that they are ints since reviews change
    # over time
    for review in df["Number of Reviews"]:
        assert isinstance(review, int)
    for percent in df["Percent Positive Reviews"]:
        assert isinstance(percent, int)


@pytest.mark.parametrize()
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
