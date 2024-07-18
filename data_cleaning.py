import pandas as pd

def clean_data(df):
    # Handle missing values using forward fill
    df = df.ffill()

    # Detect and handle outliers
    q_low = df["MonthlyCharges"].quantile(0.01)
    q_hi  = df["MonthlyCharges"].quantile(0.99)
    df = df[(df["MonthlyCharges"] >= q_low) & (df["MonthlyCharges"] <= q_hi)]

    # Address data inconsistencies
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].mean())

    return df
