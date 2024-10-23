"""
1. Filter the data to include only weekdays (Monday to Friday) and
plot a line graph showing the pedestrian counts for each day of the
week.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

df["hour_beginning"] = pd.to_datetime(df["hour_beginning"])

df["year"] = df["hour_beginning"].dt.year
df["month"] = df["hour_beginning"].dt.month
df["date"] = df["hour_beginning"].dt.date
df["day_of_week"] = df["hour_beginning"].dt.dayofweek
print(df.info())

soln1 = df.loc[df["day_of_week"] <= 4]
print(soln1.info())

"""
2. Track pedestrian counts on the Brooklyn Bridge for the year 2019
and analyze how different weather conditions influence pedestrian
activity in that year. Sort the pedestrian count data by weather
summary to identify any correlations( with a correlation matrix)
between weather patterns and pedestrian counts for the selected year.

-This question requires you to show the relationship between a
numerical feature(Pedestrians) and a non-numerical feature(Weather
Summary). In such instances we use Encoding. Each weather condition
can be encoded as numbers( 0,1,2..). This technique is called One-hot
encoding.

-Correlation matrices may not always be the most suitable
visualization method for relationships involving categorical
datapoints, nonetheless this was given as a question to help you
understand the concept better.
"""

soln2 = df.loc[df["year"] == 2019]
soln2 = soln2.sort_values(by="weather_summary")
soln2.dropna(subset=["weather_summary"], inplace=True)
print(soln2["weather_summary"].unique())
soln2["weather_summary_encoded"] = soln2["weather_summary"].astype("category").cat.codes
print(soln2["weather_summary_encoded"].count())
print(soln2["Pedestrians"].count())

correlation_matrix = soln2[["Pedestrians","weather_summary_encoded"]].corr()
# Plotting the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Pedestrians and Weather Summary')
plt.tight_layout()
plt.show()

"""
3. Implement a custom function to categorize time of day into morning,
afternoon, evening, and night, and create a new column in the
DataFrame to store these categories. Use this new column to analyze
pedestrian activity patterns throughout the day.

-Students can also show plots analyzing activity.
"""

def categorize_time_of_day(time_of_day):
    category = ""
    time_of_day = time_of_day.hour
    if time_of_day < 12:
        category = "morning"
    elif time_of_day <= 12 + 5:
        category = "afternoon"
    elif time_of_day < 12 + 8:
        category = "evening"
    else:
        category = "night"
    return category

soln3 = df
soln3.dropna(subset=["hour_beginning"], inplace=True)
soln3["categorized_time_of_day"] = soln3["hour_beginning"].dt.time.apply(categorize_time_of_day)
print(soln3.groupby("categorized_time_of_day").describe())