#Json # Serialization is the process of converting an object into a stream of bytes to store the
# object or transmit it to memory, a database, or a file. Its main purpose is to save the state
# of an object in order to be able to recreate it when needed. The reverse process is called
# deserialization.
#load loads
#dump dumps
import json

MyJson = {
    "name":"Wai Hin Soe",
    "age":18,
    "Hobby": ["AI", "football","singing"]
    }

# Loads is loading the json string into a python dictionary object.
# data = json.loads(MyJson) #Python dictionary object
#print(data)

with open("data.json", "w") as jsonFile:
    # Dumping the python dictionary object into a json string.
    json.dump(MyJson, jsonFile)