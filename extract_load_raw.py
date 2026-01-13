import pandas as pd
from sqlalchemy import create_engine

def get_engine():
    return create_engine("mysql+pymysql://root@localhost:3307/finance")


# load raw data to python
df = pd.read_csv("10k-rows.csv")
# print(f"no. of rows in data are: {len(df)}")

# connection create with mysql
engine = create_engine("mysql+pymysql://root@localhost:3307/finance")

# load/save data into mysql
df.to_sql(
    "consumer_finance_complaints_raw",
    engine,
    index=False,
    if_exists="replace",
    chunksize=1000
)

print("Data is loaded successfully")

# load mysql raw_data to python
def load_raw_from_mysql():
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM consumer_finance_complaints_raw", engine)
    return df

