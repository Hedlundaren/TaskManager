import subprocess

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
		subprocess.call([functions[id_of_function].path])
	return
		
def deploy_all(functions):
	fun_id = 0
	while(fun_id < functions[0].funCount):
		subprocess.call([functions[fun_id].path])
		fun_id += 1
	return
