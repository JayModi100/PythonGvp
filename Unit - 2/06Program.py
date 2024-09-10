import Module06 as Matrix

matrix1 = Matrix.initializeMatrix(3,3,[1,2,3,4,5,6,7,8,9])
matrix2 = Matrix.initializeMatrix(3,3,[1,2,3,4,5,6,7,8,9])


print("Matrix - 1")
Matrix.printMatrix(matrix1)
print("\nMatrix - 2")
Matrix.printMatrix(matrix2)

addition = Matrix.additionOfMatrix(matrix1,matrix2)
print("\nAddition of 2 Matrix : ")
Matrix.printMatrix(addition)

multiplication = Matrix.multiplicationOfMatrix(matrix1,matrix2)
print("Multiplication : ")
Matrix.printMatrix(multiplication)

