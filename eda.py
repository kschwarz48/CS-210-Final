import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(df):
    # Plotting age groups of customers
    plt.figure(figsize=(10, 6))
    sns.histplot(df['tenure'], bins=30)
    plt.title('Tenure Distribution of Customers')
    plt.xlabel('Tenure (months)')
    plt.ylabel('Frequency')
    plt.savefig('tenure_distribution.png')
    plt.show()
