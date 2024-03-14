import analyze_data
import requests
from bs4 import BeautifulSoup
import pandas as pd
from playwright.sync_api import sync_playwright, Playwright
import re 

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
# analyze_data.get_html_from_mostplayed

# links = analyze_data.get_game_links()
