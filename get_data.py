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
    soup = BeautifulSoup(html_content, "html.parser")
    return soup


def get_tbody(soup):
    tbody = soup.find("tbody")
    tbody = str(tbody)
    return tbody


def get_game_links(tbody):
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
        {
            "class": "popup_menu_subheader popup_genre_expand_header responsive_hidden"
        },
    )
    genres = ""
    word_list = []
    for ele in mydiv:
        elem = ele.text
        words = elem.split()
        word_list += words
        genres = "".join(words)
        print(word_list)
    genres = 
    return genres


link = "https://store.steampowered.com/app/899770/Last_Epoch/"
html = requests.get(link).content
soup = BeautifulSoup(html, "html.parser")
# Testing zone
genre = get_game_genre(soup)
percent, num = get_reviews(soup)
name = get_name(link)
print(name, percent, num, genre)
# df.loc[links.index(links[10])] = {
#     "Game Name": name,
#     "Percent Positive Reviews": percent,
#     "Number of Reviews": num,
#     "Genre": "Genre Insert",
#     "Price": "price insert",
#     "Peak Number of Players": "peak insert",
# }
