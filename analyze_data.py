import requests
from bs4 import BeautifulSoup
import pandas as pd
from playwright.sync_api import sync_playwright, Playwright
import re 

def get_html_from_mostplayed():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        # go to url
        page.goto("https://store.steampowered.com/charts/mostplayed")
        # wait for element to appear on the page:
        page.wait_for_timeout(3000)
        html_content = page.content()
        page.close()
    html_text = open("mostplayed.html", "w")
    html_text.write(html_content)
    html_text.close()

def get_game_links():
    soup = BeautifulSoup(
        open("mostplayed.html"), "html.parser"
    )
    tbody = soup.find("tbody")
    tbody = str(tbody)

    get_link = "https:\/\/store\.steampowered\.com\/app\/[^?]*\?"

    links = re.findall(get_link, tbody)
    return links

def compare_game_genre_players(game):
    """
    Finds the number of players playing a game and the games' genre.

    Args:
        game: An string representing the name of a game to analyze.

    Returns:
        A list with first value being an int of the number people who
        have left reviews, and the second value being a string of the game tag
    """
    pass


def compare_price_ratings(game):
    """
    Finds the price of the game compared to the average ratings of the game

    Args:
        game: An string representing the name of a game to analyze

    Returns:
        A list with the first value being an int representing the price, and the
        second value is a float representing the percentage ranking of reviews
    """
    pass


def compare_price_ratings_relevance(game):
    """
    Finds the price of the game compared to the average RECENT ratings of
    the game

    Args:
        game: An string representing the name of a game to analyze

    Returns:
        A list with the first value being an int representing the price, and the
        second value is a float representing the percentage ranking of reviews
    """
    pass


def compare_price_num_players(game):
    """
    Finds the price of the game compared to the number of people playing

    Args:
        game: An string representing the name of a game to analyze

    Returns:
        A list with the first value being an int representing the price, and the
        second value is a int representing the peak players in a 24h period.
    """
    pass


def compile_game_data(data, func):
    """
    Combines data from many games together to be analyzed/compared against
    each other

    Args:
        data: A Pandas dataframe containing all of the games to be analyzed

    Returns:
        A list of each functions dict that is a combination of all the dicts
        for that comparison
    """
    # loop thru the first column of the data frame which has all the game titles
    # run the helper functions for each game
    # compile each category into one list and visualize
    pass
