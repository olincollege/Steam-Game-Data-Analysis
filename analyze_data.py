def compare_game_genre_players(game):
    """
    Finds the number of players playing a game and the games' genre.

    Args:
        game: An string representing the name of a game to analyze.

    Returns:
        A list with frist value being an int of the number people who
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


def compile_game_data(path, func):
    """
    Combines data from many games together to be analyzed/compared against
    each other

    Args:
        path: A string representing the file path that contains the games to
        analyze

    Returns:
        A list of each functions dict that is a combination of all the dicts
        for that comparison
    """
    # loop thru a range of ints with each int representing a function to run
    # combine the dicts for those
    # create a dict with title of each comparison as key and the values as
    # list datapoints
    pass
