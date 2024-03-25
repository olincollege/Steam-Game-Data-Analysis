import requests
from bs4 import BeautifulSoup
import pandas as pd
from playwright.sync_api import sync_playwright, Playwright
import re


def get_html_from_mostplayed():
    """
    Retrieves the data from the official Steam website about the
    most popular games

    Args:
        None

    Returns:
        A beautiful soup object of all the html from the most played page,
        to be used to find data on each game from the list
    """

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
    soup = BeautifulSoup(html_content, "html.parser")
    return soup


def get_tbody(soup):
    """
    Finds the important body text from the html of the most played list.

    Args:
        soup: A beautiful soup object of all the html from the most played list

    Returns:
        The important content from the soup content, containing data of each
        game to be analyzed including price, peak num players, and titles
        and links to each game
    """

    tbody = soup.find("tbody")
    tbody = str(tbody)
    return tbody


def get_game_links(tbody):
    """
    Finds the links to the games on the most played list.

    Args:
        tbody: A string representing the important data of the most played
        list, derived from the function get_tbody(soup).

    Returns:
        A list of strings representing links to individual game pages.
    """

    get_link = "https:\/\/store\.steampowered\.com\/app\/[^?]*\?"

    links = re.findall(get_link, tbody)
    return links


def get_name(link):
    """
    Find the name of a game based on its link from the most played list

    Args:
        link: A string representing the link path to the game

    Returns:
        A string representing the name of the game
    """

    name = link[link.rindex("/") + 1 : -1]
    return name


def get_price_and_peak(tbody):
    """
    Finds the price and number of peak players of every game
    on the most played list.

    Args:
        tbody: A string representing the important data of the most played
        list, derived from the function get_tbody(soup).

    Returns:
        prices: A list of ints representing the cost of purchasing a game
        peak_players: A list of ints representing the peak number of players
        on a game in a 24 hour period.
    """

    # Section the html into th sections containing data we want
    sections = re.findall("<tr[^>]*>.*?</tr>", tbody)
    prices = []
    peak_players = []

    # Scan through the section for each game, adding prices and peaks
    for section in sections:
        # Find prices

        index1 = section.find("$")
        index2 = section.find("Free To Play")
        if index1 != -1:
            section = section[index1::]
            partition = section.find("</div")
            price = float(section[1:partition])
        elif index2 != -1:
            section = section[index2::]
            partition = section.find("</div")
            price = 0.0
        else:
            prices.append(-1)
            peak_players.append(-1)
            continue
        # Cut out part of section already searched
        partition = section.rfind("</td")
        section = section[:partition]
        partition = section.rfind(">")

        # Find the peak player in the readjusted section
        peak_player = section[partition + 1 : :].replace(",", "")
        peak_player = int(peak_player)

        # Add the info to the list for every game
        prices.append(price)
        peak_players.append(peak_player)
    return prices, peak_players


def get_reviews(soup):
    """
    Find the reviews and ratings of a game.

    Args:
        soup: A beautiful soup object containing all of the html info
        of a game

    Returns:
        A string representing the games reviews, extracted from the html
    """

    # Find the reviews in the html
    myspan = soup.find_all(
        "span", {"class": "nonresponsive_hidden responsive_reviewdesc"}
    )
    review = ""
    for ele in myspan:
        elem = ele.text.strip()
        words = elem.split()
        review = "".join(words)

    # Extract the wanted data

    percentage = ""
    num_reviews = ""

    # get the percentage of positive reviews
    if review.find("-") != -1:
        i = review.find("-") + 1
        while review[i] != "%":
            percentage += review[i]
            i += 1
        # get the number of reviews
    if review.find("ofthe") != -1:
        j = review.find("ofthe") + 5
        while j < review.find("userreviews"):
            num_reviews += review[j]
            j += 1

    return percentage, num_reviews


def get_game_genre(soup):
    """
    Finds the 3 most relevant tags of a game.

    Args:
        soup: A beautiful soup object containing all of the html info
        of a game

    Returns:
        A string representing the game's 3 most popular genres,
        extracted from the html
    """

    mydiv = soup.find_all(
        "div",
        {"class": "glance_tags popular_tags"},
    )
    for ele in mydiv:
        elem = ele.text
        elem = re.sub(r"\t", "", elem)
        elem = elem.strip()
        elem = elem.splitlines()
    return elem
