import pandas as pd

df = pd.read_csv("logs.csv")


df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp").reset_index(drop=True)


for ip, group in df.groupby("ip"):
    failed_count = 0
    for _, row in group.iterrows():
        if row["status"] == "FAILED":
            failed_count += 1
        elif row["status"] == "SUCCESS":
            if failed_count >= 3:
                print(f"ALERT: {ip} - {failed_count} FAILED, phir SUCCESS at {row['timestamp']}")
            failed_count = 0   # After Success reset the counter