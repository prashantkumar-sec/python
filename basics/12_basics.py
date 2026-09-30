#
# json (saving dictionary into file)
# dictionaries are not directly written so we use json module

import json

data = {
    "Prashant": 19713982738,
    "Shree": 72943729326
}

# Save
with open ("contacts.json","w") as f:
    json.dump(data, f, indent=4)

# Load
with open ("contacts.json","r") as f:
    data = json.load(f)
