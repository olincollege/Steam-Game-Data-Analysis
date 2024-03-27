import get_data
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


mostplayed_html = get_data.get_html_from_mostplayed()

tbody = get_data.get_tbody(mostplayed_html)

links = get_data.get_game_links(tbody)

prices, peak_players = get_data.get_price_and_peak(tbody)

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

count = 0
index = 0
for link in links:
    print(count, index)
    if prices[count] != -1:
        html = requests.get(link).content
        soup = BeautifulSoup(html, "html.parser")
        # Adding all of our data into the dataframe
        name = get_data.get_name(link)
        percent, num = get_data.get_reviews(soup)
        genre = get_data.get_game_genre(soup)
        
        top_genre = genre[0:4]
        while "Free to Play" in top_genre:
            top_genre.remove("Free to Play")
        df.loc[index] = {
            "Game Name": name,
            "Percent Positive Reviews": percent,
            "Number of Reviews": num,
            "First Genre": top_genre[0],
            "Second Genre": top_genre[1],
            "Third Genre": top_genre[2],
            "Price": prices[count],
            "Peak Number of Players": peak_players[count],
        }
        index += 1
    count += 1
    time.sleep(5)
df.to_csv("steam_data.csv")