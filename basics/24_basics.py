import re

logs = """Oct 12 10:41:02 sshd: Failed password for root from 203.0.113.5 port 22
Oct 12 10:42:15 sshd: Accepted password for prashant from 192.168.1.20 port 22
Oct 12 10:43:40 sshd: Failed password for admin from 203.0.113.5 port 22
Oct 12 10:44:11 sshd: Failed password for admin from 198.51.100.7 port 22
Oct 12 10:45:09 sshd: Failed password for test from 203.0.113.5 port 22"""

pattern = re.compile(r"(Failed|Accepted) password for (\w+) from ([\d.]+)")
failed = {}

for line in logs.splitlines():
    m = pattern.search(line)
    if m:
        status, user, ip = m.groups()

        if status == "Failed":
            failed[ip] = failed.get(ip, 0) + 1

for ip, count in failed.items():
    if count >= 3:
        print(f"{ip} -> {count} failed attempts ⚠️ Suspicious IP")
    else:
        print(f"{ip} -> {count} failed attempts")