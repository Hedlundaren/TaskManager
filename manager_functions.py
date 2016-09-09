import subprocess
import os
from random import randint


def search_and_deploy(function, functions):	
	fun_id = 0
	id_of_function = -1
	
	while(fun_id < functions[0].funCount):
		if(functions[fun_id].name == function):
			id_of_function = fun_id
			break
		fun_id += 1
		
	if(id_of_function == -1):
		print("No '" + function + "' exists.")
	else:
		if(functions[id_of_function].type == "exe_dir"):
			subprocess.call([functions[id_of_function].path])
		elif(functions[id_of_function].type == "music_dir"):
			os.startfile("assets\hatkarlek.mp3")
		elif(functions[id_of_function].type == "comm"):
			communicate(function)
			

	return
		
def deploy_all(functions):
	fun_id = 0
	while(fun_id < functions[0].funCount):
		subprocess.call([functions[fun_id].path])
		fun_id += 1
	return

def communicate(input):

	greetings = []
	greetings.append("Hello Simon.")
	greetings.append("Pleased to see you too, Simon.")
	greetings.append("Greetings.")
	greetings.append("Well, hello there.")
	greetings.append("Hello there, Simon.")
	greetings.append("Good day to you, Simon.")
	greetings.append("Hello Simon.")
	greetings.append("Hello Simon.")
	greetings.append("Hello Simon.")
	greeting = randint(0,len(greetings) - 1)
	print("\n" + greetings[greeting])
		
		
		
		
		
		
		
		
		
		
		