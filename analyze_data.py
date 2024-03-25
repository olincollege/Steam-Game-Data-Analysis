import pandas as pd
from playwright.sync_api import sync_playwright, Playwright
import re

def convert_csv_to_list(df):
    game_name = df["Game Name"].tolist()
    percent_positive = df["Percent Positive Reviews"].tolist()
    number_reviews = df["Number of Reviews"].tolist()
    first_genre = df["First Genre"].tolist()
    second_genre = df["Second Genre"].tolist()
    third_genre = df["Third Genre"].tolist()
    price = df["Price"].tolist()
    peak_players = df["Peak Number of Players"].tolist()

    number_reviews = [sub.replace(",", '') for sub in number_reviews]
    number_reviews = [eval(i) for i in number_reviews]
    return game_name, percent_positive, first_genre, second_genre, third_genre, price, peak_players, number_reviews

def get_number_of_positive_reviews(percent_positive, number_reviews):
    number_of_positive_reviews = []
    for i in range(len(percent_positive)):
        number_of_positive_reviews.append(int(number_reviews[i] * percent_positive[i]/100))
    return number_of_positive_reviews

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

def top_ten_most_positively_reviewed(game_name, percent_positive, peak_players):
    index_of_highest_positive = sorted(range(len(percent_positive)), key=lambda i: percent_positive[i])[-10:]
    top_reviewed_games = []
    top_reviewed_games_popularity = []
    for i in index_of_highest_positive:
        top_reviewed_games.append(game_name[i])
        top_reviewed_games_popularity.append(peak_players[i])
    return top_reviewed_games, top_reviewed_games_popularity

def top_ten_most_positive_reviews(game_name, number_of_positive_reviews, peak_players):
    index_of_top_reviewed = sorted(range(len(number_of_positive_reviews)), key=lambda i: number_of_positive_reviews[i])[-10:]
    most_reviewed_games = []
    most_reviewed_games_popularity = []
    for i in index_of_top_reviewed:
        most_reviewed_games.append(game_name[i])
        most_reviewed_games_popularity.append(peak_players[i])
    return most_reviewed_games, most_reviewed_games_popularity

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

    number_playing_genre = {key:val for key, val in number_playing_genre.items() if val > 500000}

    genre = list(number_playing_genre.keys())
    popularity = list(number_playing_genre.values()) 
    quick_sort(genre, popularity, 0, len(genre) - 1)
    return genre, popularity


def compare_game_genre_players(game):
    """
    Finds the number of players playing a game and the games' genre.

    Args:
        game: An string representing the name of a game to analyze.

    Returns:
        A list with first value being an int of the number people who
        have left reviews, and the second value being a string of the game tag
    """
    pass


def compare_price_ratings(game):
    """
    Finds the price of the game compared to the average ratings of the game

    Args:
        game: An string representing the name of a game to analyze

    Returns:
        A list with the first value being an int representing the price, and the
        second value is a float representing the percentage ranking of reviews
    """
    pass


def compare_price_ratings_relevance(game):
    """
    Finds the price of the game compared to the average RECENT ratings of
    the game

    Args:
        game: An string representing the name of a game to analyze

    Returns:
        A list with the first value being an int representing the price, and the
        second value is a float representing the percentage ranking of reviews
    """
    pass


def compare_price_num_players(game):
    """
    Finds the price of the game compared to the number of people playing

    Args:
        game: An string representing the name of a game to analyze

    Returns:
        A list with the first value being an int representing the price, and the
        second value is a int representing the peak players in a 24h period.
    """
    pass


def compile_game_data(data, func):
    """
    Combines data from many games together to be analyzed/compared against
    each other

    Args:
        data: A Pandas dataframe containing all of the games to be analyzed

    Returns:
        A list of each functions dict that is a combination of all the dicts
        for that comparison
    """
    # loop thru the first column of the data frame which has all the game titles
    # run the helper functions for each game
    # compile each category into one list and visualize
    pass
