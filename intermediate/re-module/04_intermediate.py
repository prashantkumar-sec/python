import re

line = "Failed login for user=root from 192.168.1.50"

m = re.search(r"user=(\w+) from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)

print(m.group(1))
print(m.group(2))