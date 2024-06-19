# excercises 2.1.1
# | echo: true
# | eval: false
# Save a version of your df that doesn't have any empty cells
movies_df_no_empty = movies_df_cleanv3.dropna()
print(movies_df_no_empty)

# Scan for inconsistent data
print(movies_df_no_empty['genre'].value_counts())

# Fix inconsistent data
movies_df_no_empty['genre'] = movies_df_no_empty['genre'].replace(
    "Dark Comedy", "Comedy").str.lower()
print(movies_df_no_empty['genre'].value_counts())

# Drop columns you don't need
movies_df_final = movies_df_no_empty.drop(['oscar_winner'], axis=1)
print(movies_df_final)


#
# excercises 2.1.2
# | echo: true
# | eval: true
# Additional Practice

# Add more rows
additional_movies = {
    'director': ['Christopher Nolan', 'Patty Jenkins'],
    'title_of_thing': ['Inception', 'Wonder Woman'],
    'genre': ['Sci-Fi', 'Action'],
    'year_of_release': ['2010', '2017'],
    'imdB_score': [88, 75]}
movies_df_extended['runtime'] = [120, 110, 130,
                                 115, 95, 105, 123, 95, 121, 113, 148, 141]
print(movies_df_extended.head())

# Filter movies released after 2000
movies_post_2000 = movies_df_extended[movies_df_extended['year_of_release'].astype(
    int) > 2000]
print(movies_post_2000)

# Calculate and add average score column
movies_df_extended['average_score'] = (
    movies_df_extended['imdB_score'] + movies_df_extended['rotten_tomatoes_score']) / 2
print(movies_df_extended.head())
