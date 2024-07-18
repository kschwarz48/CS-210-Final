from data_storage import store_data
from data_cleaning import clean_data
from data_transformation import transform_data
from eda import perform_eda
from sentiment_analysis import analyze_sentiment, plot_sentiment_distribution

if __name__ == "__main__":
    import pandas as pd
    import numpy as np

    # Load the dataset
    df = pd.read_csv('dataset.csv')

    # Create mock data for 'Reviews' column
    np.random.seed(0)
    df['Reviews'] = np.random.choice(['Great service!', 'Very bad experience.', 'Average.', 'Loved it!', 'Horrible!'], size=len(df))

    # Step 3: Clean data
    df = clean_data(df)

    # Step 4: Transform data
    df = transform_data(df)

    # Step 5: Perform EDA
    perform_eda(df)

    # Step 6: Perform sentiment analysis
    df = analyze_sentiment(df)
    plot_sentiment_distribution(df)

    # Step 2: Store data in databases
    store_data(df)

    # Display the final DataFrame
    print(df.head())
