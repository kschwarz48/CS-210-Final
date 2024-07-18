from sklearn.preprocessing import MinMaxScaler

def transform_data(df):
    # Example of creating a new feature
    df['tenure_per_month_charge'] = df['tenure'] / df['MonthlyCharges']

    # Normalization
    scaler = MinMaxScaler()
    df[['MonthlyCharges', 'TotalCharges']] = scaler.fit_transform(df[['MonthlyCharges', 'TotalCharges']])

    return df
