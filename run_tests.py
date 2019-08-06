#!/usr/bin/env python3
import json
import csv_tools as ct
import json_tools as jt
import postgres_tools as pt

def printHeader(str):
    print("=====================================")
    print("========= ", str)


###
###
printHeader("Read JSON and write JSON")
testData = jt.readJSONFile('test_config.json')
print(json.dumps(testData, indent=4, sort_keys=True))
jt.writeJSONFile('dummy_output.json', testData)

###
###
printHeader("Read CSV and write CSV")
result = ct.test_readFileIntoJSON()
print(json.dumps(result, indent=4, sort_keys=True))
ct.writeJSONToCSV(result, 'dummy_output.csv', 'utf8')

###
###
printHeader("Read CSV ")
result = ct.test_readFileIntoList(False)
print('Include header:', result)
result = ct.test_readFileIntoList(True)
print('Skip header:', result)

###
###
printHeader("DB Connection, insert and query")
config = pt.readJSONFile('test_config.json')
conn = pt.getConnection(config)
print('simpleQueryTest(conn):')
pt.simpleQueryTest(conn)


print("Insert Data")
import random
import string

commandStr = "INSERT INTO PERSONS (LastName, FirstName, Age) VALUES ('" + random.choice(string.ascii_letters) + "','First_A',5) ON CONFLICT ON CONSTRAINT persons_pkey DO NOTHING"
cur = pt.executeCommand(conn, commandStr, True)
if cur is not None:
    print('No cursor returned')

print('simpleQueryTest(conn):')
pt.simpleQueryTest(conn)