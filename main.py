import analyze_data
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("steam_data.csv")

game_name, percent_positive, first_genre, second_genre, third_genre, price, peak_players, number_reviews =  analyze_data.convert_csv_to_list(df)

number_of_positive_reviews, number_of_negative_reviews = analyze_data.number_of_positive_and_negative_reviews(percent_positive, number_reviews)

price_points, price_points_popularity = analyze_data.number_playing_priced_games(price, peak_players)

genre_most_popular, genre_most_popular_popularity = analyze_data.most_popular_genres(first_genre, second_genre, third_genre, peak_players)

genre_most_common, genre_most_common_number = analyze_data.most_common_genres(first_genre, second_genre, third_genre)

plt.scatter(percent_positive, peak_players)
plt.title("Positive Review Percentage vs Popularity")
plt.xlabel("Positive Review Percentage (%)")
plt.ylabel("Popularity (Peak Players over 24 Hour Period)")
plt.show() 

plt.scatter(number_of_positive_reviews, peak_players)
plt.title("Number of Positive Reviews vs Popularity")
plt.xlabel("Number of Positive Reviews")
plt.ylabel("Popularity (Peak Players over 24 Hour Period)")
plt.show()

plt.bar(price_points, price_points_popularity, color ='maroon', 
        width = 0.4)
plt.xticks(rotation = 30)
plt.title("Popularity of Games at Different Price Points")
plt.xlabel("Price Points ($)")
plt.ylabel("Popularity (Peak Players over 24 Hour Period)")
plt.show()

plt.bar(genre_most_common, genre_most_common_number, color ='maroon', 
        width = 0.4)
plt.xticks(rotation = 30)
plt.title("Number of Different Genres")
plt.xlabel("Genre")
plt.ylabel("Amount")
plt.show()

plt.bar(genre_most_popular, genre_most_popular_popularity, color ='maroon', 
        width = 0.4)
plt.xticks(rotation = 30)
plt.title("Popularity of Different Genres")
plt.xlabel("Genre")
plt.ylabel("Popularity (Peak Players over 24 Hour Period)")
plt.show()
