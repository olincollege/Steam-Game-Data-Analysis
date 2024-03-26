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


def top_ten_most_positively_reviewed(game_name, percent_positive, peak_players):
    index_of_highest_positive = sorted(
        range(len(percent_positive)), key=lambda i: percent_positive[i]
    )[-10:]
    top_reviewed_games = []
    top_reviewed_games_popularity = []
    for i in index_of_highest_positive:
        top_reviewed_games.append(game_name[i])
        top_reviewed_games_popularity.append(peak_players[i])
    return top_reviewed_games, top_reviewed_games_popularity


def top_ten_most_positive_reviews(
    game_name, number_of_positive_reviews, peak_players
):
    index_of_top_reviewed = sorted(
        range(len(number_of_positive_reviews)),
        key=lambda i: number_of_positive_reviews[i],
    )[-10:]
    most_postive_reviewed_games = []
    most_positive_reviewed_games_popularity = []
    for i in index_of_top_reviewed:
        most_postive_reviewed_games.append(game_name[i])
        most_positive_reviewed_games_popularity.append(peak_players[i])
    return most_postive_reviewed_games, most_positive_reviewed_games_popularity


def top_ten_most_negatively_reviewed(game_name, percent_positive, peak_players):
    percent_negative = [100 - percent for percent in percent_positive]
    index_of_highest_negative = sorted(
        range(len(percent_negative)), key=lambda i: percent_negative[i]
    )[-10:]
    worst_reviewed_games = []
    worst_reviewed_games_popularity = []
    for i in index_of_highest_negative:
        worst_reviewed_games.append(game_name[i])
        worst_reviewed_games_popularity.append(peak_players[i])

    return worst_reviewed_games, worst_reviewed_games_popularity


def top_ten_most_negative_negative_reviews(
    game_name, number_of_negative_reviews, peak_players
):
    index_of_top_reviewed = sorted(
        range(len(number_of_negative_reviews)),
        key=lambda i: number_of_negative_reviews[i],
    )[-10:]
    most_negative_reviewed_games = []
    most_negative_reviewed_games_popularity = []
    for i in index_of_top_reviewed:
        most_negative_reviewed_games.append(game_name[i])
        most_negative_reviewed_games_popularity.append(peak_players[i])
    return most_negative_reviewed_games, most_negative_reviewed_games_popularity


def partition(names, values, low, high):

    # choose the rightmost element as pivot
    pivot = values[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if values[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (names[i], names[j]) = (names[j], names[i])
            (values[i], values[j]) = (values[j], values[i])

    # Swap the pivot element with the greater element specified by i
    (names[i + 1], names[high]) = (names[high], names[i + 1])
    (values[i + 1], values[high]) = (values[high], values[i + 1])

    # Return the position from where partition is done
    return i + 1


# function to perform quicksort


def quick_sort(names, values, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(names, values, low, high)

        # Recursive call on the left of pivot
        quick_sort(names, values, low, pi - 1)

        # Recursive call on the right of pivot
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
