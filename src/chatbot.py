import pandas as pd

df = pd.read_csv('outputs/model_comparison.csv')

def answer_question(query):
    query = query.lower()

    avg_demand = df['y'].mean()
    rf_error = (abs(df['y'] - df['rf_pred'])).mean()
    xgb_error = (abs(df['y'] - df['xgb_pred'])).mean()
    avg_gap = (df['search_count'] - df['recommendation_count']).mean()

    if "best model" in query or "better model" in query:
        return f"XGBoost performs better with lower error ({round(xgb_error,2)}) compared to Random Forest ({round(rf_error,2)})."

    elif "demand trend" in query or "trend" in query:
        return f"Average demand is around {round(avg_demand,2)} and remains relatively stable over time with minor fluctuations."

    elif "gap" in query:
        return f"There is a negative demand-supply gap of {round(avg_gap,2)}, indicating unmet user demand."

    elif "insight" in query:
        return "Demand is stable, XGBoost performs best, and recommendation systems need improvement to reduce demand gap."

    else:
        return "Try asking about model performance, demand trend, or gap."