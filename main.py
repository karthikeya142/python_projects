# print("Hello World")
# firstname =input("enter firstname: ")
# lastname = input("enter lastname: ")
# userename=firstname+lastname
# print("username is: " +userename)
# email = userename+"@gmail.com"
# print("email is: "+email)
#
# from turtle import *
# import turtle as tur
#
# tur.penup()
# tur.left(90)
# tur.fd(200)
# tur.pendown()
# tur.right(90)
#

import pandas as pd

# Load the CSV file
ratings = pd.read_csv('C:/Users/Admin/Downloads/python/pythonProject/file.csv')


# Function to filter movies by genre
def filter_by_genre(ratings, genre):
    return ratings[ratings['genre'].str.contains(genre, case=False, na=False)]

# Function to find similar raters
def find_similar_raters(ratings, rater_id, num_top_raters):
    # Calculate similarity (simple approach: count of common ratings)
    common_ratings = ratings[ratings['rater_id'] == rater_id].merge(ratings, on='movie_id')
    common_ratings['similarity'] = common_ratings.groupby('rater_id_y')['rating_x'].transform(lambda x: x.count())
    top_raters = common_ratings.sort_values(by='similarity', ascending=False)['rater_id_y'].unique()
    return top_raters[:num_top_raters]

# Function to calculate average ratings
def calculate_average_ratings(ratings, top_raters, min_raters):
    filtered_ratings = ratings[ratings['rater_id'].isin(top_raters)]
    avg_ratings = filtered_ratings.groupby('movie_id').agg({'rating': ['mean', 'count']})
    avg_ratings.columns = ['average_rating', 'rating_count']
    return avg_ratings[avg_ratings['rating_count'] >= min_raters]

# Function to find the top-rated movie
def find_top_rated_movie(avg_ratings):
    return avg_ratings.sort_values(by='average_rating', ascending=False).iloc[0]

# Filtering movies by genre
filtered_ratings = filter_by_genre(ratings, 'Mystery')

# Finding similar raters to rater_id 964
similar_raters = find_similar_raters(filtered_ratings, 964, 20)

# Calculating average ratings for movies with at least 5 ratings
avg_ratings = calculate_average_ratings(filtered_ratings, similar_raters, 5)

# Finding the top-rated movie
top_rated_movie = find_top_rated_movie(avg_ratings)

# Output the movie with the top-rated average
print(top_rated_movie)
