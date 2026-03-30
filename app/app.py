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
df = pd.read_csv('outputs/forecast.csv')
df['ds'] = pd.to_datetime(df['ds'])

# -------------------------------
# KPI SECTION
# -------------------------------
latest_value = df['yhat'].iloc[-1]
previous_value = df['yhat'].iloc[-2]
change = latest_value - previous_value

st.metric(
    label="📈 Latest Predicted Demand",
    value=round(latest_value, 2),
    delta=round(change, 2)
)

# -------------------------------
# DATE FILTER
# -------------------------------
st.markdown("### 📅 Select Date Range")

min_date = df['ds'].min()
max_date = df['ds'].max()

date_range = st.date_input(
    "",
    [min_date, max_date]
)

if len(date_range) == 2:
    df = df[
        (df['ds'] >= pd.to_datetime(date_range[0])) &
        (df['ds'] <= pd.to_datetime(date_range[1]))
    ]

# -------------------------------
# FORECAST GRAPH
# -------------------------------
fig = px.line(
    df,
    x='ds',
    y='yhat',
    title='📈 Predicted Demand Trend'
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Demand Level",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# BUSINESS INSIGHTS
# -------------------------------
st.markdown("## 📈 Key Insights")

st.write("""
- Demand for streaming-related services is increasing  
- Seasonal spikes are visible in the trend  
- Businesses should scale infrastructure during peak periods  
""")

# -------------------------------
# RAW DATA OPTION
# -------------------------------
if st.checkbox("Show Raw Forecast Data"):
    st.dataframe(df.tail())

# -------------------------------
# BUSINESS CONTEXT
# -------------------------------
st.markdown("## 🎬 Business Context")

st.write("""
Streaming demand trends often correlate with user engagement.
Higher search interest → higher content consumption → increased infrastructure demand.

This insight can be used for:
- Infrastructure planning  
- Media workflow optimization  
- Resource allocation  
""")

# -------------------------------
# NETFLIX DATA SECTION
# -------------------------------
st.markdown("## 🎬 Netflix Viewing Insights")

try:
    netflix_df = pd.read_csv('data/watch_history.csv')

    st.write("📊 Dataset Shape:", netflix_df.shape)

    st.write("🔍 Sample Data:")
    st.dataframe(netflix_df.head())

    # Example insight (adjust column if needed)
    if 'watch_time' in netflix_df.columns:
        st.write("📈 Average Watch Time:")
        st.write(netflix_df['watch_time'].mean())

    st.write("📊 Summary Statistics:")
    st.dataframe(netflix_df.describe())

except Exception as e:
    st.warning("⚠️ Netflix dataset not loaded properly.")
    
# -------------------------------
# FINAL INSIGHT
# -------------------------------
st.markdown("## 🧠 Final Insight")

st.write("""
This system demonstrates how external demand signals (Google Trends)
can be used to forecast media demand and support supply chain decisions.

This approach helps organizations:
- Anticipate demand spikes  
- Optimize infrastructure allocation  
- Improve operational efficiency  
""")