#!/usr/bin/env python3
import json
import psycopg2

# Read JSON file into an object
def readJSONFile(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


# Write JSON Object to a file
def writeJSONFile(filename, jsonObj):
    with open(filename, 'w') as outfile:
        json.dump(jsonObj, outfile)
    return None

# Does not close the connection unless exception
def getConnection(jsonConfig):
    conn = None
    try:
        conn = psycopg2.connect(host=jsonConfig["DB_HOST"], database=jsonConfig["DB_NAME"], user=jsonConfig["DB_USER"], password=jsonConfig["DB_PASS"])
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn is not None:
            conn.close()
            conn = None
            print('Database connection closed.')
    return conn

def executeCommand(conn, commandStr, closeFlag):
    cur = None
    try:
        # create a cursor
        cur = conn.cursor()
        # execute a statement
        print('Execute:', commandStr)
        cur.execute(commandStr)
        cur.execute("COMMIT")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

        if cur is not None:
            cur.close()
            print('Database connection closed.')
            cur = None
    finally:
        if closeFlag and cur is not None:
            cur.close()
            cur = None
            print('Cursor is closed.')
    return cur

# if closeFlag is True, cursor is closed before returning
def simpleQueryTest(conn):
    cur = None
    try:
        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        print('Query PERSONS')
        cur.execute('SELECT * from PERSONS')
        # display the PERSONS
        for record in cur:
            print(record)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
            cur = None
            print('Cursor is closed.')
