import analyze_data
import get_data
import requests
from bs4 import BeautifulSoup
import pandas as pd
from playwright.sync_api import sync_playwright, Playwright
import re 
import time


mostplayed_html = get_data.get_html_from_mostplayed()

tbody = get_data.get_tbody(mostplayed_html)

links = get_data.get_game_links(tbody)

html = requests.get(links[0]).content
soup = BeautifulSoup(html, "html.parser")

"""test_link_list = links[0:3]

# for link in range(len(test_link_list)):


# make a dataframe, to be updated
dataframe_titles = {
    "Game Name": [],
    "Percent Positive Reviews": [],
    "Number of Reviews": [],
    "Genre": [],
    "Price": [],
    "Peak Number of Players": [],
}

df = pd.DataFrame(dataframe_titles)

# Adding all of our data into the dataframe
percent, num = get_data.get_reviews(soup)
df.loc[0] = {
    "Game Name": "Counter Strike 2",
    "Percent Positive Reviews": percent,
    "Number of Reviews": num,
    "Genre": "Genre Insert",
    "Price": "price insert",
    "Peak Number of Players": "peak insert",
}

df.to_csv("steam_data.csv", sep="\t")
print(f"Dataframe: \n {df}")
"""