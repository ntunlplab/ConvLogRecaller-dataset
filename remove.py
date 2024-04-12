import json
import os

with open("MultipleConflict.json", "r") as f:
    data = json.load(f)
for i, item in enumerate(data):
    del item["points"]
    data[i] = item

# save data to a new file
with open("MultipleConflict1.json", "w") as f:
    json.dump(data, f, indent=4)
