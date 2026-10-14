import re

text = "Failed login from 192.168.1.10 at 10:45"

# 1. re.search: gives the first match if the pattern is found anywhere
m = re.search(r"\d+", text)
print(m.group())      # 192

# 2. re.findall: list of all matches
print(re.findall(r"\d+", text))   # ['192', '168', '1', '10', '10', '45']

# 3. If there's no match, None comes
print(re.search(r"admin", text))  # None