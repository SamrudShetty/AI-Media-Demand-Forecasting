import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Media Demand Forecasting",
    layout="wide"
)

# -------------------------------
# TITLE
# -------------------------------
st.title("📊 AI-Powered Media Demand Forecasting Dashboard")

# -------------------------------
# LOAD DATA
# -------------------------------
forecast_df = pd.read_csv('outputs/forecast.csv')
forecast_df['ds'] = pd.to_datetime(forecast_df['ds'])

model_df = pd.read_csv('outputs/model_comparison.csv')
model_df['ds'] = pd.to_datetime(model_df['ds'])

# -------------------------------
# KPI SECTION
# -------------------------------
latest_value = model_df['y'].iloc[-1]
previous_value = model_df['y'].iloc[-2]
change = latest_value - previous_value

st.metric(
    label="📈 Latest Demand Score",
    value=round(latest_value, 2),
    delta=round(change, 2)
)

# -------------------------------
# DATE FILTER (applies to BOTH)
# -------------------------------
st.markdown("### 📅 Select Date Range")

min_date = model_df['ds'].min()
max_date = model_df['ds'].max()

date_range = st.date_input("", [min_date, max_date])

if len(date_range) == 2:
    model_df = model_df[
        (model_df['ds'] >= pd.to_datetime(date_range[0])) &
        (model_df['ds'] <= pd.to_datetime(date_range[1]))
    ]

    forecast_df = forecast_df[
        (forecast_df['ds'] >= pd.to_datetime(date_range[0])) &
        (forecast_df['ds'] <= pd.to_datetime(date_range[1]))
    ]

# -------------------------------
# MODEL COMPARISON
# -------------------------------
st.markdown("## 🤖 Model Comparison")

fig1 = px.line(
    model_df,
    x='ds',
    y=['y', 'rf_pred', 'xgb_pred'],
    title='Actual vs Model Predictions'
)

st.plotly_chart(fig1, use_container_width=True)

# -------------------------------
# FORECAST GRAPH
# -------------------------------
st.markdown("## 📈 Future Demand Forecast")

fig2 = px.line(
    forecast_df,
    x='ds',
    y='yhat',
    title='Forecasted Demand (Prophet)'
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# GAP ANALYSIS
# -------------------------------
st.markdown("## ⚖️ Demand vs Supply Gap")

model_df['gap'] = model_df['search_count'] - model_df['recommendation_count']

fig3 = px.bar(
    model_df,
    x='ds',
    y='gap',
    title='Demand-Supply Gap Over Time'
)

st.plotly_chart(fig3, use_container_width=True)

# -------------------------------
# BUSINESS INSIGHTS
# -------------------------------
st.markdown("## 💡 Business Insights")

st.write("""
- XGBoost outperforms Random Forest in demand prediction accuracy  
- Demand is primarily driven by user search behavior  
- Significant demand-supply gaps indicate missed content opportunities  
- Recommendation systems should better align with user search intent  

📊 Strategic Recommendation:
- Increase content in high-demand categories  
- Optimize recommendation algorithms  
- Invest in trending content segments  
""")

# -------------------------------
# RAW DATA
# -------------------------------
if st.checkbox("Show Raw Data"):
    st.dataframe(model_df.tail())

# -------------------------------
# FINAL INSIGHT
# -------------------------------
st.markdown("## 🧠 Final Insight")

st.write("""
This system demonstrates how multiple data signals (search, recommendations, reviews)
can be used to forecast demand and improve business decision-making.

This helps organizations:
- Anticipate demand spikes  
- Optimize content strategy  
- Improve user engagement  
""")