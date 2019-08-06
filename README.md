# python-tools
Example of leveraging existing modules or some of my own

# Run Test
python3 run_tests.py

# Install
## Setup virtualenv
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt

# Syntax checker
https://rextester.com/l/postgresql_online_compiler

# Sample PostgreSQL
http://www.postgresqltutorial.com/

-- CASCADE gets rid of dependent objects/contstraints
DROP TABLE IF EXISTS PERSONS CASCADE;

CREATE TABLE Persons (
    Personid serial,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Age int,
    PRIMARY KEY (FirstName,LastName)
);

-- See table definition information
SELECT
   COLUMN_NAME
FROM
   information_schema.COLUMNS
WHERE
   TABLE_NAME = 'persons';

SELECT
   table_name, column_name, data_type
FROM
   information_schema.COLUMNS
WHERE
   TABLE_NAME = 'persons';


-- DEFAULT promary key IS [table]_pkey : persons_pkey; 

INSERT INTO PERSONS (LastName, FirstName, Age)
VALUES ('LAST_A','First_A',5) 
ON CONFLICT ON CONSTRAINT persons_pkey 
DO NOTHING;

SELECT * FROM PERSONS;




