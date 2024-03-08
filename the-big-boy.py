import requests

r = requests.get("https://store.steampowered.com/charts/mostplayed").content
test_text = open("steam-game-HTMLs/mostplayed", "wb")
test_text.write(r)
test_text.close()
