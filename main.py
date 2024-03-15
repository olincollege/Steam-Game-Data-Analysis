import analyze_data
import get_data
import requests
from bs4 import BeautifulSoup
import pandas as pd
from playwright.sync_api import sync_playwright, Playwright
import re 
import time
import matplotlib.pyplot as plt
from collections import Counter

def under_one(value):
    if value < 3:
        return False
    return True

df = pd.read_csv("steam_data.csv")

game_name = df["Game Name"].tolist()
percent_positive = df["Percent Positive Reviews"].tolist
number_reviews = df["Number of Reviews"].tolist()
first_genre = df["First Genre"].tolist()
second_genre = df["Second Genre"].tolist()
third_genre = df["Third Genre"].tolist()
price = df["Price"].tolist()
peak_players = df["Peak Number of Players"].tolist()

genres = first_genre + second_genre + third_genre
temp = Counter(genres)
per_genre = {key:val for key, val in temp.items() if val > 5}
genre = per_genre.keys()
count = per_genre.values()

plt.bar(genre, count, color ='maroon', 
        width = 0.4)
plt.xticks(rotation = 30)
plt.show()

plt.plot(price, peak_players, "ro")
plt.show()