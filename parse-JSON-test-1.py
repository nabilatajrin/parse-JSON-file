import json
f = open('file2.json')
data = json.load(f)
f.close()
# Now you can use data as a normal dict:

for (k, v) in data.items():
   print("Key: " + k)
   print("Value: " + str(v))