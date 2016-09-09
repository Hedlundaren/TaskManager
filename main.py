

import subprocess
from manager_functions import *
from load_data import *
import time
tic = 0
toc = 0

functions = []
load_inputs(functions)


print("\n=================\n Welcome, Simon.")
print("=================")


function = input("Task: ")
function = function.lower()
print(function)
while(function != "quit" and function != "q"):
	
	if(function != "dt"):
		tic = time.clock()
	
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









