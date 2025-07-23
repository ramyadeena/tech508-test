# import json:	Loads the built-in module to work with JSON data
# json.dumps():	Converts the dictionary to a JSON string
# json.dump(): Writes the dictionary to a file in JSON format
# indent=4	:  Makes the output pretty and easy to read




import json

servers_dict = {
    "server1" :{
        "hostname":"web-server-1",
        "ip-address":"192.168.1.1",
        "role":"web",
        "status":"active"
        },
    "server2":{
        "hostname":"db-server-1",
        "ip-address":"192.168.1.2",
        "role":"database",
        "status":"maintenance"
    }
}
json_string=json.dumps(servers_dict,indent=4)

print("Json-formateed string: ")
print(type(json_string))

with open("server.json","w") as json_file: # Opens server.json in write mode and assigns it to json_file; automatically closes the file after the block.
    json.dump(servers_dict,json_file,indent=4) # indent=4 Makes the output readable by using 4 spaces for indentation
print("The dictionay has been written to 'servers.json")