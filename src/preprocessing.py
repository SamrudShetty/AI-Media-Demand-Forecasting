import pandas as pd

# Load data
df = pd.read_csv('data/pytrends_data.csv')

# Reset index if needed
df.reset_index(inplace=True)

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Rename for Prophet
df = df.rename(columns={
    'date': 'ds',
    'live streaming': 'y'
})

# Keep only required columns
df = df[['ds', 'y']]

# Save cleaned data
df.to_csv('data/cleaned_pytrends.csv', index=False)

print("✅ Cleaned data ready!")