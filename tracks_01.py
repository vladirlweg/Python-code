# Write a program that is able to read the CSV file. The program should contain
# tables, which are going to be inserted data from the CSV file.

import sqlite3

# The program should:
# 1) Connect/Disconnect to the SQLite database
# 2) Create database tables
# 3) Open and read the CSV file
# 4) Insert data into the tables

# connect to SQLite database
conn = sqlite3.connect('musical_tracks_db.sqlite')
cur = conn.cursor()

# create and reset database tables
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# open and read the CSV file
with open('tracks.csv') as f:
    for line in f:
        # strip whitespace and split the line into fields
        line = line.strip()
        pieces = line.split(',')
        if len(pieces) < 6:
            continue

        # extract fields
        name = pieces[0]
        artist = pieces[1]
        album = pieces[2]
        genre = pieces[3]
        length = pieces[4]
        rating = pieces[5]
        count = pieces[6]

        #print(name, artist, album, genre, length, rating, count)

        # insert data into the Artist table
        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
        artist_id = cur.fetchone()[0]

        # Insert data into the Genre table
        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
        genre_id = cur.fetchone()[0]

        # insert data into the Album table
        cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
        album_id = cur.fetchone()[0]

        # insert data into the Track table
        cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, genre_id, len, rating, count)
            VALUES (?, ?, ?, ?, ?, ?)''', (name, album_id, genre_id, length, rating, count))

    # commit changes
    conn.commit()

# close the connection
cur.close()