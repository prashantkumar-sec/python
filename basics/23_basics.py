import re

log = "Failed login for admin from 192.168.1.10 at 10:45"

# 1. Search: find first match
m = re.search(r"\d{1,3}(\.\d{1,3}){3}",log)
print(m.group())

# 2. findall: list of all matches
text = "Hosts: 10.0.0.1, 10.0.0.2, 172.16.5.4"
print(re.findall(r"\d{1,3}(?:\.\d{1,3}){3}", text))

# 3. groups: find parts separetly
m = re.search(r"for (\w+) from ([\d.]+)", log)
print(m.group(1), m.group(2))

# 4. sub: replace
print(re.sub(r"\d", "#", "OTP 4821"))   # OTP ####

# 5. compile: repetetive use clean code
ip_pat = re.compile(r"\d{1,3}(?:\.\d{1,3}){3}")