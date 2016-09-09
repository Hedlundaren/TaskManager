class Function:
	funCount = 0
	def __init__(self, name, path):
		self.name = name
		self.path = path
		Function.funCount += 1