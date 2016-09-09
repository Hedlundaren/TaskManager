from Colors import *

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
	print("")
	print("General info: ")
	print(platform.uname())
	print(platform.processor())
	print("")

def print_help():
	print("")
	print("There is no help here. Stupid.")
	
def list_data(functions):
	fun_id = 0
	current_type = functions[0].type
	
	print(Colors.OKBLUE, "")
	print("type: ", current_type, Colors.ENDC)
	while(fun_id < functions[0].funCount):
		
		if(functions[fun_id].type != current_type):
			current_type = functions[fun_id].type
			print("", Colors.OKBLUE)
			print("type: ", current_type, Colors.ENDC)

			
		functions[fun_id].display(functions)
		
		fun_id += 1
	print("\n")
	
	return
