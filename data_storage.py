import psycopg2
from pymongo import MongoClient

def store_in_postgresql(df, table_name):
    conn = psycopg2.connect(
        host="localhost",
        database="churn_db",
        user="kschwarz",
        password="password"
    )
    cur = conn.cursor()

    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        customerID TEXT PRIMARY KEY,
        gender TEXT,
        SeniorCitizen INTEGER,
        Partner TEXT,
        Dependents TEXT,
        tenure INTEGER,
        PhoneService TEXT,
        MultipleLines TEXT,
        InternetService TEXT,
        OnlineSecurity TEXT,
        OnlineBackup TEXT,
        DeviceProtection TEXT,
        TechSupport TEXT,
        StreamingTV TEXT,
        StreamingMovies TEXT,
        Contract TEXT,
        PaperlessBilling TEXT,
        PaymentMethod TEXT,
        MonthlyCharges FLOAT,
        TotalCharges FLOAT,
        Churn TEXT
    )
    '''
    cur.execute(create_table_query)
    conn.commit()

    for index, row in df.iterrows():
        insert_query = f"INSERT INTO {table_name} (customerID, gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Churn) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(insert_query, tuple(row))
    conn.commit()

    cur.close()
    conn.close()

def store_in_mongodb(df, collection_name):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["churn_db"]
    collection = db[collection_name]
    collection.insert_many(df.to_dict('records'))

def store_data(df):
    store_in_postgresql(df, 'customer_churn')
    store_in_mongodb(df, 'customer_churn')
