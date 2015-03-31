import sqlite3
import sys
from bs4 import BeautifulSoup
from os import path

wd = "../../tanach/x"
def processRootFile():

    # Clean database for testing
    cleanDB()

    root_file_name = path.join(wd, "x0.htm")

    soup = BeautifulSoup(open(root_file_name, mode='r', errors='replace', encoding="windows-1255"))

    # Get all the sefarim a_tags
    a_tags = soup.find_all('a')
    a_tags = a_tags[2:-1]

    sefer_files = [x['href'] for x in a_tags]
    
    all_sefer_files = []
    # Add the b sefarim
    # Indexes of 'a' sefarim
    for each in sefer_files:
        all_sefer_files.append(each)
        if 'a' in each:
            all_sefer_files.append(each.replace('a','b'))

    # torah_file_names = all_sefer_files[0:5]
    # neviim_file_names = all_sefer_files[5:26]
    # kesuvim_file_names = all_sefer_files[26:len(all_sefer_files)]

    for each in all_sefer_files:
        processEachSeferFileName(each)

def cleanDB():
    conn = sqlite3.connect("tanach_sqlite3.db")
    
    with conn:
        c = conn.cursor()

        # Commands
        print("Cleaned Pasukim Table!!!")
        c.execute("DROP TABLE IF EXISTS pasukim")
        c.execute('''CREATE TABLE pasukim
                   (Id INTEGER PRIMARY KEY, sefer_title TEXT, perek_letter TEXT, perek_index INTEGER, pasuk_letter TEXT, pasuk_index INTEGER, pasuk_text TEXT)''')

def processEachSeferFileName(file_name):

    # Determine if file is an 'a' file or a 'b' file or neither
    ab = None
    if 'a' in file_name:
        ab = 'a'
    elif 'b' in file_name:
        ab = 'b'

    # Open each file and get all the perakim file names for each sefer
    soup = BeautifulSoup(open(path.join(wd,file_name), mode='r', errors='replace', encoding="windows-1255"))
    a_tags = soup.body.p.find_all('a')

    perek_files = [x['href'] for x in a_tags]
    perek_files = perek_files[2:len(perek_files)]
    perek_files.insert(0, file_name)

    all_perek_files = []
    # Remove the doubles for a,b sefarim
    if ab is not None:
        for each in perek_files:
            if ab in each:
                all_perek_files.append(each)
    else:
        all_perek_files = perek_files

    for i in range(len(all_perek_files)):
        processEachPerek(all_perek_files[i], i + 1)

def processEachPerek(file_name, perek_number):
    soup = BeautifulSoup(open(path.join(wd,file_name), mode='r', errors='replace', encoding="windows-1255"))

    # Get metadata
    sefer_name, perek_letter = parsePerekMeta(soup)

    # Create an array of pasukim with their metadata
    text = soup.body.find_all('b')
    pasukim = []
    pasuk_number = 1
    for each in text:
        pasukim.append(
            (sefer_name,
                perek_letter,
                perek_number,
                each.text, 
                pasuk_number, 
                hebrewFilter(each.next_sibling)))
        pasuk_number += 1

    # Start database work
    conn = sqlite3.connect("tanach_sqlite3.db")

    # Create the cursor
    with conn:
        c = conn.cursor()

        # Commands
        c.executemany("INSERT INTO pasukim(sefer_title, perek_letter, perek_index, pasuk_letter, pasuk_index, pasuk_text) VALUES(?, ?, ?, ?, ?, ?)", pasukim)

def hebrewFilter(string):
    return string.replace("\xa0","").replace("\n","").replace(" {פ}","").replace(" {ס}","")

def parsePerekMeta(soup):
    h1 = soup.h1.text

    h1_split = h1.split(" ")

    sefer_name = h1_split[0]
    perek_letter = h1_split[2]
    return sefer_name, perek_letter


processRootFile()
# Create the sqlite3 connection
# conn = sqlite3.connect("tanach_sqlite3.db")

# # Create the cursor
# with conn:
# 	c = conn.cursor()

# 	# Commands
# 	c.execute("DROP TABLE IF EXISTS pasukim")
# 	c.execute('''CREATE TABLE pasukim
# 				 (Id INTEGER PRIMARY KEY, sefer_title TEXT, perek_letter TEXT, perek_index INTEGER, pasuk_letter TEXT, pasuk_index INTEGER, pasuk_text TEXT)''')
# 	string = sys.argv[1].encode('iso-8859-1').decode('windows-1255')
# 	# string = sys.argv[1].decode().encode('')
# 	soup = BeautifulSoup(sys.argv[1])
	
# 	test_tuple = (0, soup.body.h1.text, "a", 1, "A", 1, "ADSDADSF")
# 	c.execute("INSERT INTO pasukim VALUES(?,?,?,?,?,?,?)", test_tuple)
# print ("Finished")

# # getHebrew(soup.body.h1)
# print(soup)