class Matrix(object):

	numbers = []

	def __init__(self, *args):
		self.numbers = args
	
	def add(self, toAdd):
		numbers = []
		for i in range(4):
			numbers.append(self.numbers[i] + toAdd.numbers[i])
		return numbers
	def product(self, toProduct):
		numbers = [0]*4
		for i in range(2):
			for j in range(2):
				for k in range(2):
					temp = 0
					temp += (self.numbers[i+k] * toProduct.numbers[k+j])
					numbers[i+j] = temp
		return numbers