import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('outputs/forecast.csv')
df['ds'] = pd.to_datetime(df['ds'])

plt.figure(figsize=(10,5))
plt.plot(df['ds'], df['yhat'], label='Forecast')

plt.title("Demand Forecast for Streaming Trends")
plt.xlabel("Date")
plt.ylabel("Predicted Demand")
plt.legend()

# Save graph instead of just showing
plt.savefig('outputs/forecast_plot.png')

plt.show()

print("✅ Graph saved in outputs folder!")