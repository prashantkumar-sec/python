import pandas as pd

df = pd.read_csv("logs.csv") # load
print(df.head())    # first 5 rows
print(df.info())    # Columns + types
print(df["ip"])     # one Column Series
failed = df[df["status"] == "FAILED"] # filter
print(failed["ip"].value_counts())  # count per IP