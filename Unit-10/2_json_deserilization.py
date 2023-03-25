#Deserialization 
#dumps load
#dump and load work with files
#dumps and loads work with python objects
#Reverting python object into jsonDataFormat is called serialization.
#Reverting jsonDataFormat into python object is called deserialization.
import json
from textwrap import indent
myJson = { 
    "name": "Wai Hin Soe",
    "age": 18,
    "hobby": ["coding", "eating", "Artificial intelligent"]
}

# Dumps is a method that convert a python object into a json string.
# json_object = json.dumps(myJson, indent=4)
# print(type(json_object))
# pData = json.loads(json_object)
# print(type(pData))

with open("data2.json","w") as jData:
    json.dump(myJson, jData)
with open("data2.json", "r") as jsonFile:
    pData = json.load(jsonFile)
print(type(pData))
