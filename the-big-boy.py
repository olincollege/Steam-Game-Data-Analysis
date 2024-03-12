import requests
from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(
    open("steam-game-HTMLs/Grand_Theft_Auto_V.html"), "html.parser"
)
temp_text = open("temp_text", "w")
temp_text.write(soup.get_text())
temp_text.close()

myspan = soup.find_all(
    "span", {"class": "nonresponsive_hidden responsive_reviewdesc"}
)
# Take away all the extra html
for ele in myspan:
    elem = ele.text.strip()

words = elem.split()
reviews = "".join(words)

# get the percentage of positive reviews
percentage_list = []
new_percent = ""
length = len(reviews)
for index in range(length):
    if reviews[index] == "-":
        i = index + 1
        while reviews[i + 1] != "%":
            new_percent += reviews[i]
            i += 1
        percentage_list.append(new_percent)
        new_percent = ""
print(percentage_list)

# get the number of reviews


# dataset = {"Counter Strike 2": myspan[0], "Grand Theft Auto": myspan[1]}
# pd_dataset = pd.DataFrame(dataset)

# print(pd_dataset)

"""r = requests.get("https://store.steampowered.com/charts/mostplayed").content
test_text = open("steam-game-HTMLs/mostplayed", "wb")
test_text.write(r)
test_text.close()"""
