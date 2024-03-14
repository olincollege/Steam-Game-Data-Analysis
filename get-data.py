import requests
from bs4 import BeautifulSoup
import pandas as pd
from playwright.sync_api import sync_playwright, Playwright
import re

# make a dataframe, to be updated
dict = {
    "Game Name": [],
    "Percent Positive Reviews": [],
    "Number of Reviews": [],
    "Genre": [],
    "Price": [],
    "Peak Number of Players": [],
}

df = pd.DataFrame(dict)


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
    soup = BeautifulSoup(open("mostplayed.html"), "html.parser")
    tbody = soup.find("tbody")
    tbody = str(tbody)

    get_link = "https:\/\/store\.steampowered\.com\/app\/[^?]*\?"

    links = re.findall(get_link, tbody)
    return links


def get_reviews(soup):
    """
    Find the reviews and ratings of a game.

    Args:
        soup: A beautiful soup object containing all of the html info
        of a game

    Returns:
        A string representing the games reviews, extracted from the html
    """
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
    LENGTH = len(review)

    for character in range(LENGTH):
        # get the percentage of positive reviews
        if review[character] == "-":
            i = character + 1
            while review[i] != "%":
                percentage += review[i]
                i += 1
            # get the number of reviews
        if review[character : character + 5] == "ofthe":
            j = character + 5
            while review[j] != "u":
                num_reviews += review[j]
                j += 1
        # add to the existing data frame with 2 new rows
        return percentage, num_reviews


# Adding all of our data in a pandas dataframe to analyze
percent, num = get_reviews(soup)
df.append{"Game Name Insert"; percent; num; "Genre Insert"; "price insert"; "peak insert"}
pd_dataset = pd.DataFrame(dataset)
pd_dataset.index = ["Percent Positive Reviews", "Number of Reviews"]

print(f"Dataframe: \n {pd_dataset}")
