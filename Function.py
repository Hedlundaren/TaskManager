class Function:
	funCount = 0
	def __init__(self, name, path, type):
		self.name = name
		self.path = path
		self.type = type
		Function.funCount += 1
