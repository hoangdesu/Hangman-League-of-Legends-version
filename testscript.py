import json

f = open('league.json')
data = json.load(f)
print(data)
f.close()