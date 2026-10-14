import re

text = "Failed from 10.0.0.5, then failed from 172.16.0.9, success from 8.8.8.8"

pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
m = re.findall(pattern, text)
print(m)