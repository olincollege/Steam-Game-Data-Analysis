import requests
from bs4 import BeautifulSoup
import pandas as pd
from playwright.sync_api import sync_playwright, Playwright


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

soup = BeautifulSoup(
    open("steam-game-HTMLs/Grand_Theft_Auto_V.html"), "html.parser"
)
temp_text = open("temp_text", "w")
temp_text.write(soup.get_text())
temp_text.close()

    myspan = soup.find_all(
        "span", {"class": "nonresponsive_hidden responsive_reviewdesc"}
    )

    return myspan


myspan = get_html_data("steam-game-HTMLs/Grand_Theft_Auto_V.html")

# Take away all the extra html

review_list = []
for ele in myspan:
    elem = ele.text.strip()
    words = elem.split()
    review_list.append("".join(words))

print(f"Review List: {review_list}")
# Extract the wanted data

percentage_list = []
num_reviews = []
LENGTH = len(review_list)

for sentence in range(LENGTH):
    for character in range(len(review_list[sentence])):
        # get the percentage of positive reviews
        if review_list[sentence][character] == "-":
            i = character + 1
            new_percent = ""
            while review_list[sentence][i] != "%":
                new_percent += review_list[sentence][i]
                i += 1
            percentage_list.append(new_percent)
        # get the number of reviews
        if review_list[sentence][character : character + 5] == "ofthe":
            j = character + 5
            new_num = ""
            while review_list[sentence][j] != "u":
                new_num += review_list[sentence][j]
                j += 1
            num_reviews.append(new_num)

print(f"Percent List: {percentage_list}")
print(f"Num Reviews: {num_reviews}")

# Adding all of our data in a pandas dataframe to analyze
dataset = {
    "Counter Strike 2": [percentage_list[0], num_reviews[0]],
    "Grand Theft Auto": [percentage_list[1], num_reviews[1]],
}
pd_dataset = pd.DataFrame(dataset)
pd_dataset.index = ["Percent Positive Reviews", "Number of Reviews"]

print(f"Dataframe: \n {pd_dataset}")

"""r = requests.get("https://store.steampowered.com/charts/mostplayed").content
test_text = open("steam-game-HTMLs/mostplayed", "wb")
test_text.write(r)
test_text.close()"""