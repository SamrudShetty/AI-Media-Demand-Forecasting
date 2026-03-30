from prophet import Prophet
import pandas as pd
import os

# Load cleaned data
df = pd.read_csv('data/cleaned_pytrends.csv')

# Initialize model
model = Prophet()

# Train model
model.fit(df)

# Create future dates (next 90 days)
future = model.make_future_dataframe(periods=90)

# Predict
forecast = model.predict(future)

# Ensure outputs folder exists
os.makedirs('outputs', exist_ok=True)

# Save forecast
forecast.to_csv('outputs/forecast.csv', index=False)

print("✅ Forecast generated successfully!")