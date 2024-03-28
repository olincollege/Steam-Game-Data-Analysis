"""
This module runs all the data analysis functions and creates plots to visualize.
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import analyze_data

# These functions fo not have unit tests because they produce visuals

df = pd.read_csv("steam_data.csv")

(
    game_name,
    percent_positive,
    first_genre,
    second_genre,
    third_genre,
    price,
    peak_players,
    number_reviews,
) = analyze_data.convert_csv_to_list(df)

number_of_positive_reviews = analyze_data.number_of_positive_reviews(
    percent_positive, number_reviews
)

price_points, price_points_popularity = (
    analyze_data.number_playing_priced_games(price, peak_players)
)
price_points, price_points_popularity = (
    analyze_data.number_playing_priced_games(price, peak_players)
)

genre_most_common, genre_most_common_number = analyze_data.most_common_genres(
    first_genre, second_genre, third_genre
)

genre_most_popular, genre_most_popular_popularity = (
    analyze_data.most_popular_genres(
        first_genre, second_genre, third_genre, peak_players
    )
)

genre_most_common, genre_most_common_number = analyze_data.most_common_genres(
    first_genre, second_genre, third_genre
)
genre_most_common, genre_most_common_number = analyze_data.most_common_genres(
    first_genre, second_genre, third_genre
)


def create_bar_plot(x_axis, y_axis, plot_title, labelx, labely):
    """
    Creates a bar plot to compare two quanities/qualities of a game.

    Args:
        x_axis: The list of game data that is on the x-axis of the plot.
                Elements are either strings or ints.
        y_axis: The list of game data that is on the y-axis of the plot.
                Elements are either strings or ints.
        plot_title: A string representing the title of the plot
        labelx: A string representing the plots x-axis label
        labely: A string representing the plots y-axis label

    Returns:
        none
    """
    plt.bar(x_axis, y_axis, color="maroon", width=0.4)
    plt.title(plot_title)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.xticks(rotation=30)
    plt.show()


def create_scatter_plot(x_axis, y_axis, plot_title, labelx, labely):
    """
    Creates a scatter plot to compare two quanities/qualities of a game.

    Args:
        x_axis: The list of game data that is on the x-axis of the plot.
                Elements are either strings or ints.
        y_axis: The list of game data that is on the y-axis of the plot.
                Elements are either strings or ints.
        plot_title: A string representing the title of the plot
        labelx: A string representing the plots x-axis label
        labely: A string representing the plots y-axis label

    Returns:
        none
    """
    colors = cm.rainbow(np.linspace(0, 1, len(x_axis)))
    count = 0
    for c in colors:
        plt.scatter(x_axis[count], y_axis[count], color=c)
        count += 1
    plt.title(plot_title)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.show()
