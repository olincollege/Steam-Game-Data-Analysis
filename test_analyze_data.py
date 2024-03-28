"""
This module runs unit tests on the analyze_data.py file.
"""

import pytest
from analyze_data import (
    number_of_positive_reviews,
    number_playing_priced_games,
    most_popular_genres,
    most_common_genres,
)

# Functions not tested
# convert_csv_to_list: helper function using built in functions
# partition and quick_sort: general python helper functions

number_of_positive_reviews_cases = [
    # Check that empty inputs return empty
    ([], [], []),
    # Check that one percent and total reviews returns accurate value
    ([10], [20], [2]),
    # Check that multiples return correct value
    ([10, 30], [10, 100], [1, 30]),
]

number_playing_priced_games_cases = [
    # Check that price points categorize correctly 1 per category
    (
        [0.0, 11.99, 22.99, 33.99, 44.99, 55.99],
        [1, 2, 3, 4, 5, 6],
        ["Under 10", "10 - 20", "20 - 30", "30 - 40", "40 - 50", "50+"],
        [1, 2, 3, 4, 5, 6],
    ),
    # Check that prices categorize correctly with more than 1 in a category
    (
        [0.0, 9.99, 22.99, 33.99, 44.99, 55.99],
        [1, 2, 3, 4, 5, 6],
        ["Under 10", "10 - 20", "20 - 30", "30 - 40", "40 - 50", "50+"],
        [3, 0, 3, 4, 5, 6],
    ),
    # Check that empty lists return no players in every category
    (
        [],
        [],
        ["Under 10", "10 - 20", "20 - 30", "30 - 40", "40 - 50", "50+"],
        [0, 0, 0, 0, 0, 0],
    ),
]

most_popular_genres_cases = [
    # Check that empty returns all empty lists
    ([], [], [], [], [], []),
    # Check that a genres with under 500000 players are excluded
    (["Survival"], ["FPS"], ["Open World"], [499999], [], []),
    # Check that genres from the same game tie with same number of players
    (
        ["Survival"],
        ["FPS"],
        ["Open World"],
        [500001],
        ["Survival", "FPS", "Open World"],
        [500001, 500001, 500001],
    ),
    # Check that genres from multiple games are sorted correctly
    (
        ["Survival", "FPS"],
        ["FPS", "Shooter"],
        ["Open World", "Multiplayer"],
        [500001, 500001],
        ["Survival", "Open World", "Shooter", "Multiplayer", "FPS"],
        [500001, 500001, 500001, 500001, 1000002],
    ),
]

most_common_genres_cases = [
    # Check that empty genre lists returns empty rankings
    ([], [], [], [], []),
    # Check that genres occuring less than 10 times are excluded
    (
        ["Survival", "FPS"],
        ["FPS", "Shooter"],
        ["Open World", "Multiplayer"],
        [],
        [],
    ),
    # Check that if a genre occurs more than 10 times it is ranked
    (
        [
            "Survival",
            "FPS",
            "FPS",
            "FPS",
            "FPS",
            "FPS",
            "FPS",
            "FPS",
            "FPS",
            "FPS",
            "FPS",
        ],
        [
            "FPS",
            "Shooter",
            "none",
            "of",
            "these",
            "show",
            "up",
            "yay",
            "now",
            "they",
            "do",
        ],
        [
            "evil",
            "cackle",
            "you'll",
            "never",
            "take",
            "me",
            "alive",
            "hah",
            "hah",
            "hah",
            "hah",
        ],
        ["FPS"],
        [11],
    ),
    # Check that multiple genres can be ranked and sorted from every list
    (
        [
            "Survival",
            "FPS",
            "FPS",
            "FPS",
            "FPS",
            "FPS",
            "FPS",
            "FPS",
            "FPS",
            "FPS",
        ],
        [
            "FPS",
            "meme",
            "you'll",
            "never",
            "take",
            "meme",
            "meme",
            "alive",
            "meme",
            "meme",
        ],
        [
            "FPS",
            "cackle",
            "meme",
            "meme",
            "meme",
            "meme",
            "meme",
            "hah",
            "meme",
            "meme",
        ],
        ["FPS", "meme"],
        [11, 12],
    ),
]


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize(
    "percent,num_reviews,num_exp", number_of_positive_reviews_cases
)
def test_number_of_positive_reviews(percent, num_reviews, num_exp):
    """
    Tests that the correct number of positive reviews is returned based on
    the inputs.

    Args:
        percent: A list containing integers of representing the game review
        overall positivity
        num_reviews: A list containing integers of all game's number of reviews
        num_exp: A list of integers representing the expected output number of
        positive reviews
    """
    num = number_of_positive_reviews(percent, num_reviews)
    assert isinstance(num_exp, list)
    for num_value in num:
        assert isinstance(num_value, int)
    assert num == num_exp


@pytest.mark.parametrize(
    "prices,players,keys_exp,players_exp", number_playing_priced_games_cases
)
def test_number_playing_priced_games_cases(
    prices, players, keys_exp, players_exp
):
    """
    Tests that the correct number of players is added to each price category.

    Args:
        prices: A list of floats representing game prices
        players: A list of ints representing number of players
        keys_exp: A list of strings of expected output price categories
        players_exp: A list of ints expected output players in each price
        category
    """
    result_keys, result_players = number_playing_priced_games(prices, players)

    assert isinstance(result_keys, list)
    for key in result_keys:
        assert isinstance(key, str)

    assert isinstance(result_players, list)
    for player in result_players:
        assert isinstance(player, int)

    assert result_keys == keys_exp
    assert result_players == players_exp


@pytest.mark.parametrize(
    "first_genre,second_genre,third_genre,num_players,pop_genres,genre_players",
    most_popular_genres_cases,
)
def test_most_popular_genres(
    first_genre,
    second_genre,
    third_genre,
    num_players,
    pop_genres,
    genre_players,
):
    """
    Tests that the genres are sorted according to the number of players in each
    genre

    Args:
        first_genre: list of all the top first genres of the games
        second_genre: list of all the top second genres of the games
        third_genre: list of all the top third genres of the games
        num_players: list containing strings of peak player numbers of the
        games
        pop_genres: list containing strings that represent the top genres
        Ranked in ascending order based on the popularity.
        genre_players: list of integers with how popular each genre
        is. Ranked in ascending order based on the popularity.
    """
    result_genres, result_players = most_popular_genres(
        first_genre, second_genre, third_genre, num_players
    )

    assert isinstance(result_genres, list)
    for genre in result_genres:
        assert isinstance(genre, str)

    assert isinstance(result_players, list)
    for player in result_players:
        assert isinstance(player, int)

    assert result_genres == pop_genres
    assert result_players == genre_players


@pytest.mark.parametrize(
    "first_genre,second_genre,third_genre,com_genres,genre_occurances",
    most_common_genres_cases,
)
def test_most_common_genres(
    first_genre,
    second_genre,
    third_genre,
    com_genres,
    genre_occurances,
):
    """
    Tests that the genres are sorted according to the the number of
    games tagged with that genre.

    Args:
        first_genre: list of all the top first genres of the games
        second_genre: list of all the top second genres of the games
        third_genre: list of all the top third genres of the games
        com_genres: list containing strings that represent the most common
        genres. Ranked in ascending order.
        genre_occurances: list of integers with how popular each genre
        is. Ranked in ascending order based on the popularity.
    """
    result_genres, result_players = most_common_genres(
        first_genre, second_genre, third_genre
    )

    assert isinstance(result_genres, list)
    for genre in result_genres:
        assert isinstance(genre, str)

    assert isinstance(result_players, list)
    for player in result_players:
        assert isinstance(player, int)

    assert result_genres == com_genres
    assert result_players == genre_occurances
