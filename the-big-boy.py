import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("steam-game-HTMLs/Grand_Theft_Auto_V.html"), "html.parser")
temp_text = open("temp_text", "w")
temp_text.write(soup.get_text())
temp_text.close()

myspan = soup.find_all("span", {"class": "nonresponsive_hidden responsive_reviewdesc"})
print(myspan)

"""r = requests.get("https://store.steampowered.com/charts/mostplayed").content
test_text = open("steam-game-HTMLs/mostplayed", "wb")
test_text.write(r)
test_text.close()"""
