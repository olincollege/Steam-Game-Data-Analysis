"""
This module writes data from running get_data functions into a csv file.
"""

import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import get_data

# This file does not have unit tests because it has no functions

mostplayed_html = get_data.get_html_from_mostplayed()

TBODY = get_data.get_tbody(mostplayed_html)

links = get_data.get_game_links(TBODY)

prices, peak_players = get_data.get_price_and_peak(TBODY)

# make a dataframe, to be updated
dataframe_titles = {
    "Game Name": [],
    "Percent Positive Reviews": [],
    "Number of Reviews": [],
    "First Genre": [],
    "Second Genre": [],
    "Third Genre": [],
    "Price": [],
    "Peak Number of Players": [],
}

df = pd.DataFrame(dataframe_titles)

COUNT = 0
INDEX = 0
for link in links:
    print(COUNT, INDEX)
    if prices[COUNT] != -1:
        html = requests.get(link, timeout=5).content
        soup = BeautifulSoup(html, "html.parser")
        # Adding all of our data into the dataframe
        name = get_data.get_name(link)
        percent, num = get_data.get_reviews(soup)
        genre = get_data.get_game_genre(soup)

        top_genre = genre[0:4]
        while "Free to Play" in top_genre:
            top_genre.remove("Free to Play")
        df.loc[INDEX] = {
            "Game Name": name,
            "Percent Positive Reviews": percent,
            "Number of Reviews": num,
            "First Genre": top_genre[0],
            "Second Genre": top_genre[1],
            "Third Genre": top_genre[2],
            "Price": prices[COUNT],
            "Peak Number of Players": peak_players[COUNT],
        }
        INDEX += 1
    COUNT += 1
    time.sleep(5)
df.to_csv("steam_data.csv")
