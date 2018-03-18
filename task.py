from real_matrice import Matrix

if __name__ == "__main__":

	# assuming square matrix

	matrix_1 = Matrix([[4,5,1], [6,7,0], [1,2,4]])
	matrix_2 = Matrix([[2,2,3], [2,1,5], [5,2,0]])

	print('Matrix 1:')
	print(matrix_1)

	print('Matrix 2:')
	print(matrix_2)

	matrix_3 = matrix_2 + matrix_1
	print('Matrix 1 + Matrix 2 = Matrix 3:')
	print(matrix_3)

	matrix_4 = matrix_3 + 5 
	print('Matrix 3 + 5 = Matrix 4:')
	print(matrix_4)

	matrix_5 = matrix_4 - matrix_3
	print('Matrix 4 - Matrix 3 = Matrix 5:')
	print(matrix_5)

	matrix_6 = 7 - matrix_5
	print('7 - Matrix 5 = Matrix 6:')
	print(matrix_6)

	matrix_7 = matrix_5 * matrix_6
	print('Matrix 5 * Matrix 6 = Matrix 7:')
	print(matrix_7)

	matrix_8 = matrix_7 * 2
	print('Matrix 7 * 2 = Matrix 8:')
	print(matrix_8)

	double_matrix = matrix_1.double()
	for i in range(len(matrix_1.matrix)):
		print (next(double_matrix))

	matrix_9 = Matrix.creating(1,2,3,4)
	print(matrix_9)
