"""
This module compiles gathered data together to analyze and observe.
"""

"""
This module compiles gathered data together to analyze and observe.
"""

def convert_csv_to_list(df):
    """
    Converts the columns of the CSV file where we store our data to lists.

    Args:
        df: Pandas data frame containing data from CSV file
    
    Return
        lists containing the values from the columns of the CSV
    """
    game_name = df["Game Name"].tolist()
    percent_positive = df["Percent Positive Reviews"].tolist()
    number_reviews = df["Number of Reviews"].tolist()
    first_genre = df["First Genre"].tolist()
    second_genre = df["Second Genre"].tolist()
    third_genre = df["Third Genre"].tolist()
    price = df["Price"].tolist()
    peak_players = df["Peak Number of Players"].tolist()

    number_reviews = [sub.replace(",", "") for sub in number_reviews]
    number_reviews = [int(i) for i in number_reviews]
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


def number_of_positive_reviews(percent_positive, number_reviews):
    """
    Gets the number of positive reviews of all the games.

    Args:
        percent_positive: list containing integers representing the
        ratings of all the games 

        number_reviews: list containing integers with the number of 
        reivews of all the games
    
    Return:
        list containing the number of positive reviews of each game.
    """
    number_of_positive_reviews = []
    length = len(percent_positive)
    for i in range(length):
        number_of_positive_reviews.append(
            int(number_reviews[i] * percent_positive[i] / 100)
        )
    return number_of_positive_reviews


def number_playing_priced_games(prices, peak_player):
    """
    Gets number of players playing games between certain price
    points

    Args:
        prices: list containing floats of prices of each games
        peak_players: list containing ints of number of peak players of each game
    """
    price_points = {
        "Under 10": 0,
        "10 - 20": 0,
        "20 - 30": 0,
        "30 - 40": 0,
        "40 - 50": 0,
        "50+": 0,
    }
    length = len(prices)
    for i in range(length):
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
    """
    Partitions list based on pivot point and swaps values. The lists values
    and names are associated with each other in that the indices of values
    correspond to those of names. 

    Args:
        names: list with names
        values: list with values to be sorted
        low: int that is start index of partition
        high: int that is end index of partition

    Returns:
        An int that is the partition in quick_sort.
    """
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
    """
    Sorts lists names and values based on the values list using quick sort

    Parameters:
        names: list with names
        values: list with values to be sorted
        low: int that is start index of partition
        high: int that is end index of partition
    """
    if low < high:
        pi = partition(names, values, low, high)
        quick_sort(names, values, low, pi - 1)
        quick_sort(names, values, pi + 1, high)


def most_popular_genres(first_genre, second_genre, third_genre, peak_players):
    """
    Computes how many players are playing the top genres and returns lists for 
    genres that have more than 500000 players.

    Arg:
        first_genre: list containing strings of all the top first genres of the games
        second_genre: list containing strings of all the top second genres of the games
        third_genre: list containing strings of all the top third genres of the games
        peak_players: list containing strings of peak player numbers of the games
    
    Return:
        Two lists. One of which contains strings that represent the top 
        genres and the other a list of integers with how popular each genre 
        is. The lists are ranked in ascending order based on the popularity. 
    """
    number_playing_genre = {}

    length = len(first_genre)
    for index in range(length):
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
    """
    Computes how many occurances of each genre among the top 100 games and returns
    any genre with more than 7 occurances.

    Arg:
        first_genre: list of all the top first genres of the games
        second_genre: list of all the top second genres of the games
        third_genre: list of all the top third genres of the games
    
    Return:
        Two lists. One of which contains strings that represent the top 
        genres and the other a list of integers with how many occurances of each
        genre. The lists are ranked in ascending order based on the occurances. 
    """
    number_of_genre = {}
    length = len(first_genre)
    for index in range(length):
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

    number_of_genre = {
        key: val for key, val in number_of_genre.items() if val > 7
    }

    genre = list(number_of_genre.keys())
    number = list(number_of_genre.values())
    quick_sort(genre, number, 0, len(genre) - 1)
    return genre, number
