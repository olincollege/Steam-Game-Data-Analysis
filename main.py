"""
This module runs all the data analysis functions and creates plots to visualize.
"""

import pandas as pd
import matplotlib.pyplot as plt
import analyze_data

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

number_of_positive_reviews, number_of_negative_reviews = (
    analyze_data.number_of_positive_and_negative_reviews(
        percent_positive, number_reviews
    )
)

(
    top_ten_most_positively_reviewed,
    top_ten_most_positively_reviewed_popularity,
) = analyze_data.top_ten_most_positively_reviewed(
    game_name, percent_positive, peak_players
)
top_ten_most_positive_reviews, top_ten_most_positive_reviews_popularity = (
    analyze_data.top_ten_most_positive_reviews(
        game_name, number_of_positive_reviews, peak_players
    )
)

(
    top_ten_most_negatively_reviewed,
    top_ten_most_negatively_reviewed_popularity,
) = analyze_data.top_ten_most_negatively_reviewed(
    game_name, percent_positive, peak_players
)
top_ten_most_negative_reviews, top_ten_most_negative_reviews_popularity = (
    analyze_data.top_ten_most_negative_negative_reviews(
        game_name, number_of_negative_reviews, peak_players
    )
)

price_points, price_points_popularity = (
    analyze_data.number_playing_priced_games(price, peak_players)
)

genre_most_popular, genre_most_popular_popularity = (
    analyze_data.most_popular_genres(
        first_genre, second_genre, third_genre, peak_players
    )
)

plt.bar(
    top_ten_most_positively_reviewed,
    top_ten_most_positively_reviewed_popularity,
    color="maroon",
    width=0.4,
)
plt.xticks(rotation=30)
plt.show()

plt.bar(
    top_ten_most_positive_reviews,
    top_ten_most_positive_reviews_popularity,
    color="maroon",
    width=0.4,
)
plt.xticks(rotation=30)
plt.show()

plt.bar(
    top_ten_most_negatively_reviewed,
    top_ten_most_negatively_reviewed_popularity,
    color="maroon",
    width=0.4,
)
plt.xticks(rotation=30)
plt.show()

plt.bar(
    top_ten_most_negative_reviews,
    top_ten_most_negative_reviews_popularity,
    color="maroon",
    width=0.4,
)
plt.xticks(rotation=30)
plt.show()

plt.bar(price_points, price_points_popularity, color="maroon", width=0.4)
plt.xticks(rotation=30)
plt.show()

plt.bar(
    genre_most_popular, genre_most_popular_popularity, color="maroon", width=0.4
)
plt.xticks(rotation=30)
plt.show()

# plt.bar(top_reviewed_games, top_reviewed_games_number_playing, color ='maroon',
#         width = 0.4)
# plt.xticks(rotation = 30)
# plt.show()

# plt.plot(price, peak_players, "ro")
# plt.show()
