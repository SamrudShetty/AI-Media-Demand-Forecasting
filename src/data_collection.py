from pytrends.request import TrendReq
import pandas as pd

# Connect to Google Trends
pytrends = TrendReq(hl='en-US', tz=330)

# Keywords for your project
keywords = ["live streaming", "OTT platforms", "sports streaming"]

# Get data for last 5 years
pytrends.build_payload(keywords, timeframe='today 5-y')

# Fetch data
data = pytrends.interest_over_time()

# Remove unwanted column
data = data.drop(columns=['isPartial'])

# Save file
import os

os.makedirs('data', exist_ok=True)
data.to_csv('data/pytrends_data.csv')

print("✅ Pytrends data saved successfully!")