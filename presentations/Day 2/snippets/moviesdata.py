import pandas as pd #importing the pandas module
# initialise some list objects that contains our data, this could also be a list of lists, or a dict of lists for example
import numpy as np #importing a module to allow me to include 'missing data

director = ['John Carpenter', '', 'Nicolas Winding Refn', 'Matthijs van Heijningen', 'Damien Chazelle', 'Dennis Villanueve', 'Coen Brothers', 'Kelly Asbury', 'Edgar Wright', 'Coen Brothers']
names = ['The Thing', 'Blade Runner 2049', 'Drive',  'The Thing', 'Whiplash', 'Arrival', 'No Country for Old Men', 'Shrek 2', 'Hot Fuzz', 'Fargo']
genre = ['Horror', 'Sci-Fi', 'Action', 'Horror', 'Drama', 'Sci-Fi', 'Drama', 'Comedy', 'Comedy', 'Dark Comedy']
year = ['1982', '2017', '2011', '2011', '2014', '2016', '2007', '2004', '2007', '1996']
imdb_score = [82, 80, 78, 62, np.nan, 79, 82, 73, 78, 81]
rt_critics = [82, 88, 93, 34, np.nan, 94, 93, 89, 91, 94]
lead = ['male', 'Male', 'm', 'Female', 'm', 'Male', 'fem', 'Orgre', 'Male', 'Male']
cry = ["No", "No", "No", "No", "No", "Yes", "No", "Yes", "No", "No"]
movies_df = pd.DataFrame(
    list(zip(director, names, genre, year, imdb_score, rt_critics, lead, cry)), # first argument, passing a list of lists to the zip function
    columns = ['Participant Name', 'Title of Thing', 'Genre', 'Year of Release', 'ImdB Score', 'Rotten Tomatoes Score ', 'Gender of Lead', "Make Me Cry?"]# second argument , passing a list to the columns arguments
    )# closing the first pair of brackets to complete the function call