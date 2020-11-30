import json

f = open("NumAEvenNumBOdd.json", "r")
mystr = f.read()

obj = json.loads(mystr)

print(obj)
