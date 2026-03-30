# 📊 AI Media Demand Forecasting System

## 🚀 Overview
This project is an AI-based media demand forecasting system that predicts which content will be popular by analyzing Google Trends (PyTrends) and user watch history.  
It combines data preprocessing, feature engineering, and machine learning to generate actionable insights and visual forecasts.  
The workflow includes data collection, modeling, visualization, and an app-based execution for easy use.

*Additional datasets such as movies, users, reviews, search logs, and recommendation logs will be integrated in future phases.*

---

## 🎯 Key Features
- 📦 Data pipeline for multiple datasets  
- 🧹 Data preprocessing & cleaning  
- 📈 Trend analysis using PyTrends data  
- 🤖 Machine learning-based demand forecasting  
- 📊 Visualization of predictions  
- 🖥️ App-based execution (`app.py`)  

---

## 📂 Project Structure
AI-Media-Demand-Forecasting/
│
├── app/
│ └── app.py # Main application entry point
│
├── data/ # Raw & cleaned datasets
│ ├── movies.csv
│ ├── users.csv
│ ├── watch_history.csv
│ ├── reviews.csv
│ ├── search_logs.csv
│ ├── recommendation_logs.csv
│ ├── pytrends_data.csv
│ └── cleaned_pytrends.csv
│
├── src/ # Core logic
│ ├── data_collection.py
│ ├── preprocessing.py
│ ├── model.py
│ └── visualize.py
│
├── outputs/ # Results
│ ├── forecast.csv
│ └── forecast_plot.png
│
├── requirements.txt
└── README.md



---

## 🔍 Workflow

1. **Data Collection**  
   - Collect Google Trends and watch history data  

2. **Data Preprocessing**  
   - Clean missing values  
   - Feature engineering  

3. **Model Building**  
   - Train machine learning model to predict demand  

4. **Forecast Generation**  
   - Generate future demand forecasts  

5. **Visualization**  
   - Create graphical representations of forecast results  

---

## 📊 Datasets Used

Currently used datasets:

- 📈 Google Trends (PyTrends)  
- ⏱️ Watch history  

*Other datasets like movies, users, reviews, search logs, and recommendation logs are reserved for future development phases.*

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/SamrudShetty/AI-Media-Demand-Forecasting.git
cd AI-Media-Demand-Forecasting

2. Install dependencies
pip install -r requirements.txt

3. Run the application
python app/app.py

📈 Output
The model generates:
Forecasted demand data saved as outputs/forecast.csv
Visualization plot saved as outputs/forecast_plot.png

🧠 Technologies Used
Python
Pandas & NumPy
Scikit-learn
Matplotlib / Seaborn

🔮 Future Enhancements
Deploy as an interactive web app (Streamlit)
Add real-time data integration
Incorporate deep learning models (LSTM)
Integrate additional datasets for richer forecasting and recommendations

💼 Real-World Applications
OTT platforms like Netflix and Prime Video
Content recommendation engines
Marketing and trend analysis
Inventory and demand planning

👨‍💻 Author
Samrud Shetty
GitHub: https://github.com/SamrudShetty


⭐ If you find this project useful

Please give it a star ⭐ on GitHub!



---

	
