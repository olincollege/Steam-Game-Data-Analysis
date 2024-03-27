"""
This module compiles gathered data together to analyze and observe.
"""


def convert_csv_to_list(df):
    game_name = df["Game Name"].tolist()
    percent_positive = df["Percent Positive Reviews"].tolist()
    number_reviews = df["Number of Reviews"].tolist()
    first_genre = df["First Genre"].tolist()
    second_genre = df["Second Genre"].tolist()
    third_genre = df["Third Genre"].tolist()
    price = df["Price"].tolist()
    peak_players = df["Peak Number of Players"].tolist()

    number_reviews = [sub.replace(",", "") for sub in number_reviews]
    number_reviews = [eval(i) for i in number_reviews]
    return (
        game_name,
        percent_positive,
        first_genre,
        second_genre,
        third_genre,
        price,
        peak_players,
        number_reviews,
    )


def number_of_positive_and_negative_reviews(percent_positive, number_reviews):
    number_of_positive_reviews = []
    number_of_negative_reviews = []
    for i in range(len(percent_positive)):
        number_of_positive_reviews.append(
            int(number_reviews[i] * percent_positive[i] / 100)
        )
        number_of_negative_reviews.append(
            int(number_reviews[i] * (100 - percent_positive[i]) / 100)
        )
    return number_of_positive_reviews, number_of_negative_reviews

def number_playing_priced_games(prices, peak_player):
    price_points = {
        "Under 10": 0,
        "10 - 20": 0,
        "20 - 30": 0,
        "30 - 40": 0,
        "40 - 50": 0,
        "50+": 0,
    }
    for i in range(len(prices)):
        if prices[i] < 10:
            price_points["Under 10"] += peak_player[i]
        elif prices[i] < 20:
            price_points["10 - 20"] += peak_player[i]
        elif prices[i] < 30:
            price_points["20 - 30"] += peak_player[i]
        elif prices[i] < 40:
            price_points["40 - 50"] += peak_player[i]
        elif prices[i] < 50:
            price_points["40 - 50"] += peak_player[i]
        else:
            price_points["50+"] += peak_player[i]
    return list(price_points.keys()), list(price_points.values())


def partition(names, values, low, high):
    pivot = values[high]

    i = low - 1

    for j in range(low, high):
        if values[j] <= pivot:
            i = i + 1
 
            (names[i], names[j]) = (names[j], names[i])
            (values[i], values[j]) = (values[j], values[i])

    (names[i + 1], names[high]) = (names[high], names[i + 1])
    (values[i + 1], values[high]) = (values[high], values[i + 1])

    return i + 1
 
def quick_sort(names, values, low, high):
    if low < high:
        pi = partition(names, values, low, high)
        quick_sort(names, values, low, pi - 1)
        quick_sort(names, values, pi + 1, high)


def most_popular_genres(first_genre, second_genre, third_genre, peak_players):
    number_playing_genre = {}

    for index in range(len(first_genre)):
        first = first_genre[index]
        second = second_genre[index]
        third = third_genre[index]
        if first not in number_playing_genre:
            number_playing_genre[first] = peak_players[index]
        else:
            number_playing_genre[first] += peak_players[index]
        if second not in number_playing_genre:
            number_playing_genre[second] = peak_players[index]
        else:
            number_playing_genre[second] += peak_players[index]
        if third not in number_playing_genre:
            number_playing_genre[third] = peak_players[index]
        else:        
            number_playing_genre[third] += peak_players[index]

    number_playing_genre = {
        key: val for key, val in number_playing_genre.items() if val > 500000
    }

    genre = list(number_playing_genre.keys())
    popularity = list(number_playing_genre.values())
    quick_sort(genre, popularity, 0, len(genre) - 1)
    return genre, popularity

def most_common_genres(first_genre, second_genre, third_genre):
    number_of_genre = {}
    for index in range(len(first_genre)):
        first = first_genre[index]
        second = second_genre[index]
        third = third_genre[index]
        if first not in number_of_genre:
            number_of_genre[first] = 1
        else:
            number_of_genre[first] += 1
        if second not in number_of_genre:
            number_of_genre[second] = 1
        else:
            number_of_genre[second] += 1
        if third not in number_of_genre:
            number_of_genre[third] = 1
        else:        
            number_of_genre[third] += 1

    number_of_genre = {key:val for key, val in number_of_genre.items() if val > 5}

    genre = list(number_of_genre.keys())
    number = list(number_of_genre.values()) 
    quick_sort(genre, number, 0, len(genre) - 1)
    return genre, number
