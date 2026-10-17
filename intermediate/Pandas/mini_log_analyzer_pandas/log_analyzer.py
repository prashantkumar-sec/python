import pandas as pd

df=pd.read_csv("log.csv")

print("Total rows: ",len(df))  # total number of rows

failed = df[df["status"] =="FAILED"]
print("Total failed:", len(failed))

print(failed["ip"].value_counts())

for ip, count in failed["ip"].value_counts().items():
    if count>=3:
        print(f"SUSPICIOUS {ip} ({count} failed attempts)")

success = df[df["status"] == "SUCCESS"]

fail_counts = failed["ip"].value_counts()
bad_ips = fail_counts[fail_counts >= 3].index

compromised = success[success["ip"].isin(bad_ips)]

for ip in compromised["ip"]:
    print(f"ALERT: {ip} failed 3+ times, then login success!")