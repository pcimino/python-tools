#!/usr/bin/env python3
import json
import csv_tools as ct
import json_tools as jt

testData = jt.readJSONFile('test_config.json')
print(json.dumps(testData, indent=4, sort_keys=True))
jt.writeJSONFile('dummy_output.json', testData)

result = ct.test_readFileIntoJSON()
print(json.dumps(testData, indent=4, sort_keys=True))
ct.writeJSONToCSV(result, 'dummy_output.csv', 'utf8')
