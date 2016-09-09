
from Function import *



"""
This file is only for loading data of different types.
"""


def load_inputs(functions):	

	
	
	null = ""
	
	### Executables ###
	
	chrome = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
	git = 'C:\Program Files\Git\git-bash.exe'
	gp = "C:\Program Files (x86)\Guitar Pro 5\GP5.exe"
	py = "C:\Program Files (x86)\Python35\python.exe"
	
	functions.append(Function("c", chrome, "exe_dir"))
	functions.append(Function("git", git, "exe_dir"))
	functions.append(Function("gp", gp, "exe_dir"))
	functions.append(Function("py", py, "exe_dir"))
	functions.append(Function("calc", py, "exe_dir"))

	### Greetings ###
	functions.append(Function("hi", null, "comm"))
	functions.append(Function("hii", null, "comm"))
	functions.append(Function("hiii", null, "comm"))
	functions.append(Function("hiiii", null, "comm"))
	functions.append(Function("hiiiii", null, "comm"))
	functions.append(Function("hello", null, "comm"))
	functions.append(Function("helloo", null, "comm"))
	functions.append(Function("hellooo", null, "comm"))
	functions.append(Function("wazzap", null, "comm"))
	functions.append(Function("wassup", null, "comm"))
	functions.append(Function("wassap", null, "comm"))
	functions.append(Function("good day", null, "comm"))
	functions.append(Function("hellew", null, "comm"))
	functions.append(Function("good evening", null, "comm"))
	functions.append(Function("hi motherfucker", null, "comm"))
	functions.append(Function("ni hao", null, "comm"))
	functions.append(Function("ni hao bitch", null, "comm"))
	functions.append(Function("ni hao bithc", null, "comm"))
	functions.append(Function("ni hao bith", null, "comm"))
	
	
	### Info ###
	functions.append(Function("time", null, "info"))
	functions.append(Function("i", null, "info"))
	functions.append(Function("help", null, "info"))
	functions.append(Function("list", null, "info"))
	
	### Music and Sounds ###
	tour = "assets\hatkarlek.mp3"
	functions.append(Function("tour", tour, "music_dir"))
	
def load_greetings(greetings):
	greetings.append("Hello Simon.")
	greetings.append("Pleased to see you too, Simon.")
	greetings.append("Greetings.")
	greetings.append("Well, hello there.")
	greetings.append("Hello there, Simon.")
	greetings.append("Good day to you, Simon.")
	greetings.append("Hello Simon.")
	greetings.append("Hello Simon.")
	greetings.append("Hello Simon.")
	