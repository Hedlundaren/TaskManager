

class Function:
	funCount = 0
	
	def __init__(self, name, path, type):
		self.name = name
		self.name1 = name.partition(' ')[1]
		self.name2 = name.partition(' ')[2]
		self.path = path
		self.type = type
		Function.funCount += 1
			
	def display(self, array):
		print("name: ", self.name)
