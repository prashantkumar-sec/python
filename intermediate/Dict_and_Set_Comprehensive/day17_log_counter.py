# DAY 17 - Log Counter

log = [
    "prashant,192.168.1.10,FAILED",
    "admin,10.0.0.5,FAILED",
    "prashant,192.168.1.10,SUCCESS",
    "admin,10.0.0.5,FAILED",
    "guest,172.16.0.8,FAILED",
    "admin,10.0.0.9,FAILED",
    "prashant,192.168.1.11,FAILED",
    "guest,172.16.0.8,SUCCESS",

    # Added logs
    "admin,10.0.0.5,FAILED",
    "admin,10.0.0.5,FAILED",
    "prashant,192.168.1.12,SUCCESS",
    "hacker,192.168.1.50,FAILED",
]

# 1. Unique IPs
unique_ips = {entry.split(",")[1] for entry in log}

# 2. Count failed attempts per IP
failed_count = {
    ip: sum(
        1
        for entry in log
        if entry.split(",")[1] == ip and entry.split(",")[2] == "FAILED"
    )
    for ip in unique_ips
}

# 3. Suspicious IPs - 3 or more failed attempts
suspicious = {
    ip: count
    for ip, count in failed_count.items()
    if count >= 3
}

# 4. Output
print("Unique IPs:", unique_ips)
print("Failed Count:", failed_count)
print("Suspicious IPs:", suspicious)# DAY 17 - Log Counter

log = [
    "prashant,192.168.1.10,FAILED",
    "admin,10.0.0.5,FAILED",
    "prashant,192.168.1.10,SUCCESS",
    "admin,10.0.0.5,FAILED",
    "guest,172.16.0.8,FAILED",
    "admin,10.0.0.9,FAILED",
    "prashant,192.168.1.11,FAILED",
    "guest,172.16.0.8,SUCCESS",

    # Added logs
    "admin,10.0.0.5,FAILED",
    "admin,10.0.0.5,FAILED",
    "prashant,192.168.1.12,SUCCESS",
    "hacker,192.168.1.50,FAILED",
]

# 1. Unique IPs
unique_ips = {entry.split(",")[1] for entry in log}

# 2. Count failed attempts per IP
failed_count = {
    ip: sum(
        1
        for entry in log
        if entry.split(",")[1] == ip and entry.split(",")[2] == "FAILED"
    )
    for ip in unique_ips
}

# 3. Suspicious IPs - 3 or more failed attempts
suspicious = {
    ip: count
    for ip, count in failed_count.items()
    if count >= 3
}

# 4. Output
print("Unique IPs:", unique_ips)
print("Failed Count:", failed_count)
print("Suspicious IPs:", suspicious)