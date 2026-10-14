import re

line = "Failed login for user=admin from 10.0.0.5"

m = re.search(r"user=(\w+) from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)

print(m.group(0))
print(m.group(1))
print(m.group(2))