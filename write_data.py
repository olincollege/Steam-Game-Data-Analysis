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


# Adding all of our data in a pandas dataframe to analyze
dataset = {
    "Counter Strike 2": [get_data.get_reviews(soup)],
}
pd_dataset = pd.DataFrame(dataset)
pd_dataset.index = ["Percent Positive Reviews", "Number of Reviews"]

print(f"Dataframe: \n {pd_dataset}")
