import sqlite3
import sys
from bs4 import BeautifulSoup as bs

# Open the file in binary
# soup = bs(open("../../tanach/x/x0101.htm", mode='r', errors='replace', encoding="windows-1255" ))

# Create the sqlite3 connection
conn = sqlite3.connect("tanach_sqlite3.db")

# Create the cursor
with conn:
	c = conn.cursor()

	# Commands
	c.execute("DROP TABLE IF EXISTS pasukim")
	c.execute('''CREATE TABLE pasukim
				 (Id INTEGER PRIMARY KEY, sefer_title TEXT, perek_letter TEXT, perek_index INTEGER, pasuk_letter TEXT, pasuk_index INTEGER, pasuk_text TEXT)''')

	soup = BeautifulSoup(sys.argv[1])
	
	test_tuple = (0, soup.body.h1.text, "a", 1, "A", 1, "ADSDADSF")
	c.execute("INSERT INTO pasukim VALUES(?,?,?,?,?,?,?)", test_tuple)
print ("Finished")

# getHebrew(soup.body.h1)
print(soup)