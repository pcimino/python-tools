#!/usr/bin/env python3
import json

# Read JSON file into an object
def readJSONFile(filename):
    with open(filename) as json_file:
        data = json.load(json_file)

    return data


# Write JSON Object to a file
def writeJSONFile(filename, jsonObj):
    with open(filename, 'w') as outfile:
        json.dump(jsonObj, outfile)

testData = readJSONFile('test_config.json')

print(json.dumps(testData, indent=4, sort_keys=True))

writeJSONFile('dummy_output.json', testData)