import pandas as pd

movies = pd.read_csv('data/movies.csv')
users = pd.read_csv('data/users.csv')
reviews = pd.read_csv('data/reviews.csv')
search_logs = pd.read_csv('data/search_logs.csv')
recommendation_logs = pd.read_csv('data/recommendation_logs.csv')

print(search_logs.columns)
print(reviews.columns)
print(recommendation_logs.columns)

# Rename columns
search_logs.rename(columns={'search_date': 'date'}, inplace=True)
reviews.rename(columns={'review_date': 'date'}, inplace=True)
recommendation_logs.rename(columns={'recommendation_date': 'date'}, inplace=True)

# Convert to datetime
search_logs['date'] = pd.to_datetime(search_logs['date'])
reviews['date'] = pd.to_datetime(reviews['date'])
recommendation_logs['date'] = pd.to_datetime(recommendation_logs['date'])

# 🔥 IMPORTANT: Remove time BEFORE grouping
search_logs['date'] = search_logs['date'].dt.date
reviews['date'] = reviews['date'].dt.date
recommendation_logs['date'] = recommendation_logs['date'].dt.date

# Now group
search_demand = search_logs.groupby('date').size().reset_index(name='search_count')

recommendation_volume = recommendation_logs.groupby('date').size().reset_index(name='recommendation_count')

reviews_count = reviews.groupby('date').size().reset_index(name='review_count')


print(search_demand.head())
print(recommendation_volume.head())
print(reviews_count.head())


# Merge all dataset
df = search_demand.merge(recommendation_volume, on='date', how='outer')
df = df.merge(reviews_count, on='date', how='outer')

df.fillna(0, inplace=True)


#Create Demand Score
df['demand_score'] = (
    df['search_count'] * 0.5 +
    df['recommendation_count'] * 0.3 +
    df['review_count'] * 0.2
)


#Gap Feature
df['demand_supply_gap'] = df['search_count'] - df['recommendation_count']

#Prepare Model
df.rename(columns={'date': 'ds', 'demand_score': 'y'}, inplace=True)

df['ds'] = pd.to_datetime(df['ds'])

#Final Dataset
df.to_csv('data/final_dataset.csv', index=False)

print("✅ Final dataset ready for modeling!")

print(df.head())