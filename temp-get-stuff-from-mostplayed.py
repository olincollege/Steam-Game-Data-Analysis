import requests
from bs4 import BeautifulSoup
import pandas as pd
from playwright.sync_api import sync_playwright, Playwright
import re 


soup = BeautifulSoup(
    open("mostplayed.html"), "html.parser"
)
tbody = soup.find("tbody")
tbody = str(tbody)

get_link = "https:\/\/store\.steampowered\.com\/app\/[^?]*\?"

links = re.findall(get_link, tbody)

