from extract_load_raw import load_raw_from_mysql
from extract_load_raw import get_engine
import pandas as pd
df=load_raw_from_mysql()

#1.removing duplicate values 
dup_count = df.duplicated().sum()
print("Duplicate rows:", dup_count)

df = df.drop_duplicates()

#2. handling missing values-
#checking & filling null values
df=df.fillna(0)

print(df.isnull().sum())

# 2. fixing datatypes
#dates
print(df["date_received"].dtype,df["date_sent_to_company"].dtype)

df["date_received"]=pd.to_datetime(df["date_received"],errors="coerce")
df["date_sent_to_company"]=pd.to_datetime(df["date_sent_to_company"],errors="coerce")

print(df["date_received"].dtype,df["date_sent_to_company"].dtype)

#3.creating/adding new columns-

# month
df["Month_of_receiving"] = df["date_received"].dt.month

# year
df["Year_of_receiving"] = df["date_received"].dt.year

# complaints in each month
df["no_of_complaints_each_month"] = df.groupby("Month_of_receiving")["Month_of_receiving"].transform("count")

# complaints in each year
df["no_of_complaints_each_year"] = df.groupby("Year_of_receiving")["Year_of_receiving"].transform("count")

# days to send complaint to company
df["days_to_send"] = (df["date_sent_to_company"] - df["date_received"]).dt.days

# followup date
df["followup_date"] = df["date_received"] + pd.Timedelta(days=7)

print(f'''showing new added columns:
    {df[[
    "Month_of_receiving",
    "no_of_complaints_each_month",
    "no_of_complaints_each_year",
    "days_to_send",
    "followup_date"
]].head(10)}''')
#loading clean/transformed data in mysql
df.to_sql(
    "consumer_finance_complaints_clean",
    con=get_engine(),
    index=False,
    chunksize=1000,
    if_exists="replace"
)
print("clean data loaded successfully")

