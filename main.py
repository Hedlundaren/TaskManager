import subprocess
import os
import time

from functions.manager_functions import *
from functions.load_data import *
from Class.Colors import *

tic = 0
toc = 0

import sqlite3
conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM
cursor = conn.cursor()

# # create a table
# cursor.execute("""CREATE TABLE albums
                  # (title text, artist text, release_date text, 
                   # publisher text, media_type text) 
               # """)
 
#cursor.execute("INSERT INTO albums VALUES ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')")
#conn.commit()
sql = """
UPDATE albums 
SET artist = 'John Doe' 
WHERE artist = 'Andy Hunter'
"""
cursor.execute(sql)

# sql = """
# DELETE FROM albums
# WHERE artist = 'John Doe'
# """
# cursor.execute(sql)

ref = "John Doe"
for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
	if(ref == row[2]):
		print("WOO")
		
sql = "SELECT * FROM albums"
cursor.execute(sql)
print(cursor.fetchall())  # or use fetchone()
 


 
 
 
print(Colors.OKGREEN, "\n=================\n Welcome, Simon.")
print("=================")
print("", Colors.ENDC)

# Load functions
functions = []
load_inputs(functions)

# Ask user for task
function = input("Task: ")	
function = function.lower()

print(function)
while(function != "quit" and function != "q"):
	
	if(function != "dt"):
		tic = time.clock()
	
	if(function == "qq"):
		os.startfile("")
		
	if(function != "" and function != "quit" and function != "q"):
		if(function == "all"):
			deploy_all(functions)
		elif(function == "dt"):
			print_delta_time(tic, toc)
		else:
			search_and_deploy(function, functions)		
	
	
	if(function != "dt"):
		toc = time.clock()
		
	function = input("Task: ")
	function = function.lower()









