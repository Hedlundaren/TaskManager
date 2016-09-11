from Class.Colors import *
from functions.load_data import *
from random import randint
import time

def get_delta_time(tic, toc):
	return toc - tic

def print_delta_time(tic, toc):
	deltaTime = get_delta_time(tic, toc)
	print("")
	mess = deltaTime
	print(mess)
	return

def print_general_info():
	import platform
	print(Colors.HEADER)
	print("General info: ")
	print(platform.uname())
	print(platform.processor())
	print(Colors.ENDC)

def print_help():
	print("")
	print("There is no help here. Stupid.")
	
def list_data(functions, function):
	
	type = function.partition(" ")[2]
	
	fun_id = 0
	current_type = functions[0].type
	if(type == '.'):
		print(Colors.OKBLUE, "")
		print("type: ", current_type, Colors.ENDC)
	else:
		print(Colors.OKBLUE, "")
		print("type: ", type, Colors.ENDC)

	while(fun_id < functions[0].funCount):
		
		if(type == '.'):
			if(functions[fun_id].type != current_type):
				current_type = functions[fun_id].type
				print("", Colors.OKBLUE)
				print("type: ", current_type, Colors.ENDC)
			functions[fun_id].display(functions)
		
		elif(functions[fun_id].type == type):
			print("name: ", functions[fun_id].name, Colors.ENDC)
		fun_id += 1
	print("\n")
	
	return

def interpret_input(input):
	response_found = False
	
	# Answer question
	answers = []
	load_answers(answers)
	if(input[-1:] == '?' or input[-2:] == '?!'):
		answer = randint(0,len(answers) - 1)
		response_found = True
		print(Colors.OKGREEN, "\n" + answers[answer], Colors.ENDC)
		time.sleep(0.6)
	
	# Check cursing
	curse_words = []
	load_curse_words(curse_words)
	word_id = 0
	while(word_id < len(curse_words)):
		part_id = 0
		parts = input.partition(" ")
		while(part_id < len(parts)):
			if(parts[part_id] == curse_words[word_id]):
				print("", Colors.OKGREEN)
				print("Are you angry, Simon?", Colors.ENDC)
				response_found = True
			part_id += 1
		word_id += 1
		
	# specific answers
	if(input == "thank you"):
		print("", Colors.OKGREEN)
		print("You are welcome.", Colors.ENDC)
		response_found = True
		
	if(input == "yolo"):
		print("", Colors.OKGREEN)
		print("You only live once, Simon.", Colors.ENDC)
		response_found = True
		
	if(response_found == False):
		print(input, "is a weird input.")