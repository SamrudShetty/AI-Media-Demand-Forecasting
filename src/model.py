from prophet import Prophet
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv('data/final_dataset.csv')
df['ds'] = pd.to_datetime(df['ds'])

# -------------------------------
# PROPHET MODEL
# -------------------------------
prophet_df = df[['ds', 'y']]

model = Prophet()
model.fit(prophet_df)

future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

# -------------------------------
# FEATURE ENGINEERING (ONLY ONCE)
# -------------------------------
df['day'] = df['ds'].dt.day
df['month'] = df['ds'].dt.month
df['year'] = df['ds'].dt.year

X = df[['day', 'month', 'year']]
y = df['y']

# -------------------------------
# RANDOM FOREST
# -------------------------------
rf = RandomForestRegressor()
rf.fit(X, y)
rf_preds = rf.predict(X)

# -------------------------------
# XGBOOST
# -------------------------------
xgb = XGBRegressor()
xgb.fit(X, y)
xgb_preds = xgb.predict(X)

# -------------------------------
# MODEL COMPARISON
# -------------------------------
print("RF MAE:", mean_absolute_error(y, rf_preds))
print("XGB MAE:", mean_absolute_error(y, xgb_preds))

# -------------------------------
# SAVE OUTPUTS
# -------------------------------
os.makedirs('outputs', exist_ok=True)

df['rf_pred'] = rf_preds
df['xgb_pred'] = xgb_preds

df.to_csv('outputs/model_comparison.csv', index=False)
forecast[['ds', 'yhat']].to_csv('outputs/forecast.csv', index=False)

print("✅ Forecast + Model Comparison saved successfully!")