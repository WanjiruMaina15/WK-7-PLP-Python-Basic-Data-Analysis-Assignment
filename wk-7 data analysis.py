import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')


#Upload file

#Read the file into a pandas dataframe
#Display the first few rows of the dataset using .head() to inspect the data.

try:####Error handling for file not found
    olympics = pd.read_csv('olympics2024.csv')
    print(olympics.head())
except FileNotFoundError:
    print("Error: The file 'olympics2024.csv' was not found. Please check the path.")
    exit()  # stops the program if the file doesn't exist
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
    exit()
except pd.errors.ParserError:
    print("Error: Could not parse the CSV file. Please check its format.")
    exit()


#Explore the structure of the dataset by checking the data types and any missing values.
print(olympics.info())
     
#Clean the dataset by either filling or dropping any missing values.
olympics=olympics.dropna()
print(olympics)

#Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using .describe().
print(olympics.describe())

#Perform groupings on a categorical column (for example, species, region, or department) and compute the mean of a numerical column for each group.
grouped_data = olympics.groupby('Country')['Gold'].mean().sort_values(ascending=False)
print(grouped_data)



#Identify any patterns or interesting findings from your analysis.
#Use group to calculate the average population size for each continent
population_mean=olympics.groupby('Continent')['Population'].mean()
     
print(population_mean)

#Task 3: Data Visualization
# rename 'GDP per capita (current US$)'
olympics = olympics.rename(columns={'GDP per capita (current US$)' : 'GDPpc' })
olympics

#create at least four different types of visualizations:
#Piechart showing trends over time (for example, a time-series of sales data).
# geneate a table with only the European countries gold medal counts
eu_gold = olympics.where(olympics['Continent'] == 'Europe').where(olympics['Gold'] > 0).dropna().sort_values('Gold', ascending=False)[['Country', 'Gold']]
eu_gold
# create pie chart
plots.figure(figsize=(8,8))
plots.pie(eu_gold['Gold'], labels=eu_gold['Country'], autopct='%1.1f%%', startangle=90)



#Bar chart showing the comparison of a numerical value across categories (e.g., average petal length per species).
# calculate the average medals of each type (gold, silver, bronze) obtained by
# each contiment
medal_aves = olympics.pivot_table(index='Continent', values=['Gold','Silver','Bronze'], aggfunc='mean')[['Gold','Silver','Bronze']]
medal_aves
# plot the bar chart
medal_aves.plot(kind='bar', color=['gold','silver','#cd7f32'])

#Histogram of a numerical column to understand its distribution.
# Draw a histogram of Total medals
olympics.hist('Total', bins=np.arange(0,130,5))
plots.title('Total Medals by country')
plots.xlabel('Total Medals')
plots.ylabel('Frequency')

# Create a histogram with Seaborn
sns.histplot(data=olympics, x='Total', hue='Continent', multiple='stack', bins=26)

# Add labels and title
plots.xlabel('Total Medals')
plots.ylabel('Frequency')
plots.title('Histogram of Total Medals by Continent')


#Scatter plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length).
# use a scatter plot to see if there is a relationship between a country's
print(olympics)
# polulation size and the number of gold medals the country obtained
olympics.plot.scatter(x='Population', y='Gold',title='Population vs Gold Medals')
plots.show()

#Customize your plots with titles, labels for axes, and legends where necessary.