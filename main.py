import subprocess
from manager_functions import *
from Function import *
		
chrome = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
git = 'C:\Program Files\Git\git-bash.exe'
gp = "C:\Program Files (x86)\Guitar Pro 5\GP5.exe"
py = "C:\Program Files (x86)\Python35\python.exe"
tour = "assets\hatkarlek.mp3"
null = ""

functions = []

### Executables ###
functions.append(Function("c", chrome, "exe_dir"))
functions.append(Function("git", git, "exe_dir"))
functions.append(Function("gp", gp, "exe_dir"))
functions.append(Function("py", py, "exe_dir"))

### Greetings ###
functions.append(Function("hi", null, "comm"))
functions.append(Function("hello", null, "comm"))
functions.append(Function("wazzap", null, "comm"))
functions.append(Function("wassup", null, "comm"))
functions.append(Function("good day", null, "comm"))
functions.append(Function("hellew", null, "comm"))
functions.append(Function("good evening", null, "comm"))
functions.append(Function("hi motherfucker", null, "comm"))
functions.append(Function("ni hao", null, "comm"))
functions.append(Function("ni hao bitch", null, "comm"))

### Music and Sounds ###
functions.append(Function("tour", tour, "music_dir"))


print("\n=================\n Welcome, Simon.")
print("=================")


function = input("Task: ")
function = function.lower()
print(function)
while(function != "quit" and function != "q"):
	
	if(function != "" and function != "quit" and function != "q"):
		if(function == "all"):
			deploy_all(functions)
		else:
			search_and_deploy(function, functions)		
	
	function = input("Task: ")
	function = function.lower()









