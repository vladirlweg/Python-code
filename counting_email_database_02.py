# Write a program that is able to open a database and create a table.
# The program should be able to extract all email addresses from the text file
# inputed from the user.The program should be able to count the number of
# appearances of each organization found in email addresses and add it to the 
# created table.
# The table should contain two columns, one for organization and one for number
# of counts.

import sqlite3
import re

# The program should do the followings:
# 1) Open the database
# 2) Create the table
# 3) Input user and open the file
# 4) Extract the email addresses from the lines
# 5) Extract the organization from each email
# 6) If the organization does not exist add a new row. If it exists then update the count


# open the database
conn = sqlite3.connect('email_counts_02.sqlite')
cur = conn.cursor()

# create table
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)
''')

# input from user
fname = input('Enter file name: ')

if (len(fname)<1): 
    fname = 'mbox-short.txt'

fh = open(fname)
for line in fh:
    if line.startswith('From:'):
        # extract the email address from the line
        pieces = line.split()
        email = pieces[1]
        # extract organization from email address
        domain = re.findall('@(.+)', email)
        if domain:
            domain = domain[0]
            
            # check if the domain already exists in the database
            cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
            row = cur.fetchone()
            
            # if the domain does not exist then insert a new row
            if row is None:
                cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
            # if the domain does exists then update the counts
            else:
                cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))
    
# commit the changes after processing all the lines
conn.commit()
    
# query and print the results
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10')
for row in cur.fetchall():
    print(str(row[0]),row[1])

cur.close()