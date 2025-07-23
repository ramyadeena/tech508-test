import json

with open('server.json','r') as file:
    servers = json.load(file) #  Parse the JSON content from the file into a Python dictionary called 'servers'

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
