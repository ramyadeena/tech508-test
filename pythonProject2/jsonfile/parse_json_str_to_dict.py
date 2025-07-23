import json

with open('server.json','r') as jsonfile:

    #jsonstr = jsonfile.read()
    #servers = json.loads(jsonfile) # TypeError: the JSON object must be str, bytes or bytearray, not TextIOWrapper

    #Read the entire file content into a string
    jsonstr = jsonfile.read()

    #Parse the JSON string into a Python dictionary
    servers= json.loads(jsonstr)

    #Rule to remember:
    # load() = file
    # loads() = string

#json.load()	Reading JSON from a file	File object
#json.loads()	Reading JSON from a string (e.g. API)	String (str)

#print the type to see wheyher it is dictionary

print(type(servers))

#print the server1 and 2 record

print("server1 record :" ,servers['server1'])
print("server2 record: ", servers['server2'])

#print all key and value pair:

for key,value in servers.items():
    print(f"key and value :'{key}' ='{value}'")
    for sub_key, sub_value in value.items():
        print(f"  Record key and sub value: '{sub_key}' = '{sub_value}'")
