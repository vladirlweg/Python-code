# Write a program that is able to handle tables using many-to-many approach
# to store enrolment and role data.

import json
import sqlite3

# The program should:
# 1) Connect/Disconnect to the SQLite database
# 2) Create database tables
# 3) Open and load JSON file
# 4) Parse JSON data and insert data into the tables


# connect to SQLite database
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# create tables and reset the database
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

# open and load the JSON data file
fname = 'roster_data.json'
with open(fname) as f:
    data = json.load(f)

# parse JSON data and populate the database
for entry in data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    # insert User
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    # insert Course
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    # insert Member with role
    cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)',(user_id, course_id, role))

# commit changes and close connection
conn.commit()
cur.close()