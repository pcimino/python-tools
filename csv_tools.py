#!/usr/bin/env python3
import sys
import csv
import codecs
import re
import json

# Convert text strings into valid JSON key strings
# Strips special char
# makes UPPER
def convertStringToKey(strVal):
    # Tried slugify but throws "NameError: name 'unicode' is not defined"

    strVal = (re.sub('[^A-Za-z0-9 _]', '', strVal)).upper();
    strVal = strVal.replace(' ', '_')
    while strVal.__contains__('__'):
        strVal = strVal.replace('__', '_')
    return strVal

# Assumes first row is header
# encode e.g. utf8, ascii, etc
#
# NOTE only creates
# jsonObjectList with a simple structure
#
# and all keys matching columns present, null/empty must be present if no value
# [
#   { 'columnHeader_1' : 'rowValue_1', ... 'columnHeader_n' : 'rowValue_n' }
#   { 'columnHeader_1' : 'rowValue_1', ... 'columnHeader_n' : 'rowValue_n' }
# ]
def readFileIntoJSONList(filename, encode):
    inFile = open(filename, 'rt', encoding=encode)
    reader = csv.reader(inFile)
    keys = []
    jsonObjectList = []

    row = next(reader)
    for col in row:
        keys.append(convertStringToKey(col))
    print(keys)
    for row in reader:
        jsonString=""
        for index,col in enumerate(row):
            jsonString += '"' + keys[index] + '":"' + col + '",'
        jsonString = '{' + jsonString[0:-1] + '}'
        jsonObjectList.append(json.loads(jsonString))
    inFile.close()
    return jsonObjectList

# Get the KEYs from simple JSON Object
def getJSONObjectKeys(jsonObject):
    keys = []
    for key in jsonObject.keys():
        print(key)
        keys.append(key)
    return keys

# Get the KEYs from simple JSON LIST
def getJSONListKeys(jsonObjectList):
    return getJSONObjectKeys(jsonObjectList[0])

# encode e.g. utf8, ascii, etc
# NOTE only handles
# jsonObjectList with a simple structure
#
# and all keys matching columns present, null/empty must be present if no value
# [
#   { 'columnHeader_1' : 'rowValue_1', ... 'columnHeader_n' : 'rowValue_n' }
#   { 'columnHeader_1' : 'rowValue_1', ... 'columnHeader_n' : 'rowValue_n' }
# ]
def writeJSONToCSV(jsonObjList, filename, encode):
    keys = []
    if len(jsonObjList) > 0:
        keys = getJSONListKeys(jsonObjList)
    else:
        return None

    # Probably should use csv writer to be consistent
    # this was easier to work with
    outFile = codecs.open(filename, "w", encode)

    colCount = 0
    maxCol = len(keys)-1

    # Open file to write
    # Print header row
    rowStr = ""
    for key in keys:
        rowStr += key
        if (colCount < maxCol):
            rowStr += ','
        else:
            rowStr += '\n'
        colCount+=1

    outFile.write(rowStr)

    # Print data rows
    for entry in jsonObjList:
        rowStr = ""
        colCount = 0
        for key in keys:
            rowStr += entry[key]
            if (colCount < maxCol):
                rowStr += ','
            else:
                rowStr += '\n'
            colCount += 1

        outFile.write(rowStr)

    # Close file
    outFile.close()

def test_convertStringToKey():
    testStr = "Test this ^%$&#*()@! 1234567890 STRing"
    expectedStr = "TEST_THIS_1234567890_STRING"
    print("TEST:", testStr)
    print("EXPECT:", expectedStr)
    print("RESULT:", convertStringToKey(testStr))

def test_readFileIntoJSON():
    result = readFileIntoJSONList('test_read.csv', 'utf8')
    return result
