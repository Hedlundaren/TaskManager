
from Class.Function import *



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
	premier ="C:\Program Files\Adobe\Adobe Premiere Pro CS5.5\Adobe Premiere Pro.exe"
	
	functions.append(Function("c", chrome, "exe"))
	functions.append(Function("git", git, "exe"))
	functions.append(Function("gp", gp, "exe"))
	functions.append(Function("py", py, "exe"))
	functions.append(Function("calc", py, "exe"))
	functions.append(Function("premier", premier, "exe"))

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
	functions.append(Function("helllew", null, "comm"))
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
	functions.append(Function("list .", null, "info"))
	functions.append(Function("list exe", null, "info"))
	functions.append(Function("list comm", null, "info"))
	functions.append(Function("list music", null, "info"))
	functions.append(Function("list info", null, "info"))
	functions.append(Function("list ai", null, "info"))
	
	### AI ###
	memory = "memory/memory.txt"
	functions.append(Function("mem .", memory, "ai"))
	functions.append(Function("mem add", memory, "ai"))
	functions.append(Function("mem clean", memory, "ai"))
	functions.append(Function("mem del", memory, "ai"))
	
	### Music and Sounds ###
	tour = "assets\hatkarlek.mp3"
	kissepaus = "assets\kissepaus.mp3"
	functions.append(Function("tour", tour, "music"))
	functions.append(Function("kissepaus", kissepaus, "music"))
	
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
	
def load_curse_words(curse_words):
	curse_words.append("motherfucker")
	curse_words.append("fan")
	curse_words.append("perkele")
	curse_words.append("helvete")
	curse_words.append("fuck")
	curse_words.append("fuuck")
	curse_words.append("shit")
	curse_words.append("cunt")
	
def load_answers(answers):
	answers.append("Good question, Simon.")
	answers.append("I sure know the answer.")
	answers.append("You should know.")
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	