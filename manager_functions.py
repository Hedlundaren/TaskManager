

import subprocess
import os
import time
from random import randint
from load_data import load_greetings

def get_delta_time(tic, toc):
	return toc - tic

def print_delta_time(tic, toc):
	deltaTime = get_delta_time(tic, toc)
	print("\n")
	mess = deltaTime
	print(mess)
	return


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
	print("no")
		
	
def communicate(input):
	greetings = []
	load_greetings(greetings)
	greeting = randint(0,len(greetings) - 1)
	print("\n" + greetings[greeting])
	time.sleep(0.6)
		
		
		
		
		
		
		
		
		
		
		