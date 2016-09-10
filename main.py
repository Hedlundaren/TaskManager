

import subprocess
from manager_functions import *
from load_data import *
from Colors import *
import os
import time
tic = 0
toc = 0

functions = []
load_inputs(functions)


print(Colors.OKGREEN, "\n=================\n Welcome, Simon.")
print("=================")
print("", Colors.ENDC)


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









