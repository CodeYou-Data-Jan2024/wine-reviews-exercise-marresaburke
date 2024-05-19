import pandas as pd

#Read in CSV file
wine_reviews = pd.read_csv("../wine-reviews-exercise-marresaburke/data/winemag-data-130k-v2.csv.zip", index_col = 0)
wine_reviews
#Find how many reviews per country
data_wine = wine_reviews.country.value_counts()
data_wine
#Find the average points per country
country_avg = wine_reviews.groupby('country').points.mean().round(decimals=1) 
country_avg

#Build new dataframe with data

compliled = pd.DataFrame({'count': data_wine, 'points': country_avg})
compliled
final_data = compliled.sort_values('count', ascending= 0)
final_data
#Save new dataframe to new csv file

final_data.to_csv('../data/reviews-per-country.csv')




