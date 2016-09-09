

# External 
import subprocess
import os
import time
from random import randint
from datetime import datetime

# Includes
from load_data import load_greetings
from sub_manager_functions import *



	

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
		
		### Executables ###
		if(functions[id_of_function].type == "exe_dir"):
			p = subprocess.call([functions[id_of_function].path])
		
		### Music ###
		elif(functions[id_of_function].type == "music_dir"):
			music(functions[id_of_function].path)
		
		### Info ###
		elif(functions[id_of_function].type == "info"):
			info(functions[id_of_function].name)
			
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
	
def music(path):
	os.startfile(path)
	
def info(info):
	if(info == "time"):
		print("")
		print("Executed time: ", time.clock())
		print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	if(info == "i"):
		print_general_info()
	if(info == "help"):
		print_help()
		
def communicate(input):
	greetings = []
	load_greetings(greetings)
	greeting = randint(0,len(greetings) - 1)
	print("\n" + greetings[greeting])
	time.sleep(0.6)
	
		
		
		
		
		
		
		
		
		
		