import pandas as pd

#Read in CSV file
<<<<<<< HEAD
wine_reviews = pd.read_csv('../data/winemag-data-130k-v2.csv.zip', index_col = 0)

#Find how many reviews per country
#data_wine = wine_reviews.country.value_counts()

=======
wine_reviews = pd.read_csv("../wine-reviews-exercise-marresaburke/data/winemag-data-130k-v2.csv.zip", index_col = 0)
wine_reviews
#Find how many reviews per country
data_wine = wine_reviews.country.value_counts()
data_wine
>>>>>>> e09e9b18063def561141352291525ed8bcdb8735
#Find the average points per country
#country_avg = wine_reviews.groupby('country').points.mean().round(decimals=1) 

#Build new dataframe with data

<<<<<<< HEAD
#compliled = pd.DataFrame({'count': data_wine, 'points': country_avg})
#final_data = compliled.sort_values('count', ascending= 0)

#Save new dataframe to new csv file
#final_data.to_csv('reviews-per-country.csv')
=======
compliled = pd.DataFrame({'count': data_wine, 'points': country_avg})
compliled
final_data = compliled.sort_values('count', ascending= 0)
final_data
#Save new dataframe to new csv file

final_data.to_csv('../data/reviews-per-country.csv')

>>>>>>> e09e9b18063def561141352291525ed8bcdb8735



