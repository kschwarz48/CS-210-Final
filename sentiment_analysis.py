from textblob import TextBlob

def analyze_sentiment(df):
    def analyze(review):
        analysis = TextBlob(review)
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    df['sentiment'] = df['Reviews'].apply(analyze)
    return df

def plot_sentiment_distribution(df):
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(10, 6))
    sns.countplot(x='sentiment', data=df)
    plt.title('Sentiment Distribution of Customer Reviews')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.savefig('sentiment_distribution.png')
    plt.show()
