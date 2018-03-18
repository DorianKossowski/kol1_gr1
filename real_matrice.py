from math import sqrt, floor

class Matrix(object):

	def __init__(self, args):
		self.matrix = args
		self.dimension = len(args)

	def __str__(self):
		output = ''
		for i in range(self.dimension):
			output += '| '
			for j in range(self.dimension):
				output += str(self.matrix[i][j]) + ' '
			output += '|\n'
		return output
	
	def __add__(self, toAdd):
		result_matrix = Matrix([[0 for _ in range(self.dimension)] for _ in range(self.dimension)])
		if isinstance(toAdd, self.__class__):
			if self.dimension == len(toAdd.matrix):
				for i in range(self.dimension):
					for j in range(self.dimension):
						result_matrix.matrix[i][j] = self.matrix[i][j] + toAdd.matrix[i][j]
				return result_matrix
			else:
				print("Different sizes!")
		else:
			for i in range(self.dimension):
				for j in range(self.dimension):
					result_matrix.matrix[i][j] = self.matrix[i][j] + toAdd	
			return result_matrix

	def __radd__(self, toAdd):
		result_matrix = Matrix([[0 for _ in range(self.dimension)] for _ in range(self.dimension)])
		for i in range(self.dimension):
			for j in range(self.dimension):
				result_matrix.matrix[i][j] = self.matrix[i][j] + toAdd
		return result_matrix

	def __sub__(self, toSubtract):
		return (self + (toSubtract*(-1)))

	def __rsub__(self, toSubtract):
		return ((toSubtract + self*(-1)))

	def __mul__(self, toMultiply):
		result_matrix = Matrix([[0 for _ in range(self.dimension)] for _ in range(self.dimension)])
		if isinstance(toMultiply, self.__class__):
			if self.dimension == len(toMultiply.matrix):
				for i in range(self.dimension):
					for j in range(self.dimension):
						for k in range(self.dimension):
							result_matrix.matrix[i][j] += self.matrix[i][k] * toMultiply.matrix[k][j]
				return result_matrix
			else:
				print("Different sizes!")
		else:
			for i in range(self.dimension):
				for j in range(self.dimension):
					result_matrix.matrix[i][j] = self.matrix[i][j] * toMultiply	
			return result_matrix

	def __rmul__(self, toMultiply):
		result_matrix = Matrix([[0 for _ in range(self.dimension)] for _ in range(self.dimension)])
		for i in range(self.dimension):
			for j in range(self.dimension):
				result_matrix.matrix[i][j] = self.matrix[i][j] * toMultiply
		return result_matrix	

	def double(self):
		print('Doubling of matrix: \n{}'.format(self))
		for i in range(self.dimension):
			self.matrix[i] = [x**2 for x in self.matrix[i]]
			yield self.matrix[i]

	@staticmethod
	def creating(*numbers):
		size = len(numbers)
		if not sqrt(size) == floor(sqrt(size)):
			print('\nNeed square amount of numbers')
		else:
			print('\nCreating new matrix based on {}'.format(numbers))
			dim = int(sqrt(size))
			result_matrix = Matrix([numbers[i*dim:i*dim+dim] for i in range(dim)])
			result_matrix.dimension = dim
			return result_matrix			