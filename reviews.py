import pandas as pd

#Read in CSV file
wine_reviews = pd.read_csv('../data/winemag-data-130k-v2.csv.zip', index_col = 0)

#Find how many reviews per country
#data_wine = wine_reviews.country.value_counts()

#Find the average points per country
#country_avg = wine_reviews.groupby('country').points.mean().round(decimals=1) 

#Build new dataframe with data

#compliled = pd.DataFrame({'count': data_wine, 'points': country_avg})
#final_data = compliled.sort_values('count', ascending= 0)

#Save new dataframe to new csv file
#final_data.to_csv('reviews-per-country.csv')



