
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
	