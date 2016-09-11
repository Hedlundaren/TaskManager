# External 
import subprocess
import os
import time

from random import randint
from datetime import datetime

# Includes
from functions.load_data import load_greetings
from functions.sub_manager_functions import *



def search_and_deploy(function, functions):	
	fun_id = 0
	id_of_function = -1
	
	while(fun_id < functions[0].funCount):
		if(functions[fun_id].name == function):
			id_of_function = fun_id
			break
		fun_id += 1
		
	if(id_of_function == -1):
		# Input is not registered
		interpret_input(function)
	else:
		
		### Executables ###
		if(functions[id_of_function].type == "exe"):
			exe(functions, id_of_function)
				
		### Music ###
		elif(functions[id_of_function].type == "music"):
			music(functions[id_of_function].path)
		
		### Info ###
		elif(functions[id_of_function].type == "info"):
			info(functions[id_of_function].name, functions)
			
		### Info ###
		elif(functions[id_of_function].type == "ai"):
			AI(functions, id_of_function)
			
		### Communication ###
		elif(functions[id_of_function].type == "comm"):
			communicate(function)
			
	return
		
def deploy_all(functions):
	fun_id = 0
	while(fun_id < functions[0].funCount):
		subprocess.call([functions[fun_id].path])
		fun_id += 1
	return

def exe(functions, id):
	if(functions[id].name == "py" or functions[id].name == "calc"):
		p = subprocess.call([functions[id].path])
	else:
		subprocess.Popen([functions[id].path], shell=True)
		
def music(path):
	os.startfile(path)
	
def info(info, functions):
	if(info == "time"):
		print("")
		print("I have been alive for: ", time.clock())
		print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	elif(info == "i"):
		print_general_info()
	elif(info == "help"):
		print_help()
	elif(info[:4] == "list"):
		list_data(functions, info)
		
def communicate(input):
	greetings = []
	load_greetings(greetings)
	greeting = randint(0,len(greetings) - 1)
	print(Colors.OKGREEN, "\n" + greetings[greeting], Colors.ENDC)
	time.sleep(0.6)
	
def AI(functions, id):
	
	if(functions[id].name == "mem ."):
		display_memory(functions[id].path)
	if(functions[id].name == "mem add"):
		add_memory(functions[id].path)
	if(functions[id].name == "mem clean"):
		open(functions[id].path, 'w').close()
	if(functions[id].name == "mem del"):
		del_memory(functions[id].path)
		
def add_memory(path):
	print("", Colors.OKGREEN)
	new_mem = input("Add memory: ")
	print(Colors.ENDC)
	file = open(path, 'a')
	file_input = "\n" + new_mem
	file.write(file_input)
	file.close()
	display_memory(path)
	
def del_memory(path):	
	f = open(path,"r")
	lines = f.readlines()
	f.close()
	f = open(path,"w")
	h = str(input("Delete memory: "))
	h = h + "\n"
	for line in lines:
		if(line != h):
			f.write(line)
	f.close()
		
def display_memory(path):
	print(Colors.WARNING)
	file = open(path, 'r+')
	print(file.read(), Colors.ENDC)
	file.close()
		