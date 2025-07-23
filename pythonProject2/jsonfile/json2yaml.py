import json
import os
import sys
import yaml

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")
    exit(1)

# 1. Convert the JSON to YAML - use yaml library
yaml_data = yaml.dump(source_content, sort_keys=False) # it converts python dictionary into yaml string.

if len(sys.argv) > 2:
    target_file_name = sys.argv[2]
    if os.path.exists(target_file_name):
        print("ERROR: " + target_file_name + " already exists")
    else:
        with open(target_file_name, "w") as target_file:
            target_file.write(yaml_data) # convert yaml string to yaml file.

        print("YAML file created: " + target_file_name)

else:
    # No target filename provided, so print YAML to the console
    print("No target file specified. Outputting YAML to the console:\n")
    print(yaml_data)
# fo better safety , potential for extra checking.