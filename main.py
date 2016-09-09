import subprocess
from manager_functions import *
from Function import *
		
chrome = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
git = 'C:\Program Files\Git\git-bash.exe'
gp = "C:\Program Files (x86)\Guitar Pro 5\GP5.exe"
py = "C:\Program Files (x86)\Python35\python.exe"

functions = {}
functions[0] = Function("c", chrome)
functions[1] = Function("git", git)
functions[2] = Function("gp", gp)
functions[3] = Function("py", py)

print("\n=================\n Welcome, Simon.")
print("=================")


function = input("Task: ")

while(function != "quit" and function != "q"):
	
	if(function != "" and function != "quit" and function != "q"):
		if(function == "all"):
			deploy_all(functions)
		else:
			search_and_deploy(function, functions)		
	
	function = input("Task: ")









