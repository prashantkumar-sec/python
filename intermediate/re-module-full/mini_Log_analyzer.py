# Task: Create a Mini Log Analyzer

import re

pattern = r"for (\w+) from (\d{1,3}\.\d{1,3}\.\d{1,3})"

try:
    with open("auth.log", "r") as f:
        for line in f:
            if "Failed" in line:
                m = re.search(pattern, line)
                if m:
                    user =m.group(1)
                    ip = m.group(2)
                    print(user, ip)
except FileNotFoundError:
    print("File not found")
