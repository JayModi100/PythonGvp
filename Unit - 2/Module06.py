def initializeMatrix(row,col,value):
    if row*col != len(value):
        print("Value is Missing")
        return
    item=0
    matrix = []
    for i in range(row):
        row = []
        for j in range(col):
            row.append(value[item])
            item+=1
        matrix.append(row)
    
    return matrix

def printMatrix(matrix):
    for row in matrix:
        for col in row:
            print(col,end="   ")
        print()



def additionOfMatrix(matrix1,matrix2):

    if(len(matrix1) != len(matrix1)):
        return "Error"
    # matrix initialization
    matrix = []
    for row in range(len(matrix1)):
        matrix.append([])
        for col in range(len(matrix1[row])):
            matrix[row].append(matrix1[row][col]+matrix2[row][col])
    return matrix


# def multiplicationOfMatrix(matrix1,matrix2):
#     matrix = []
#     for row in range(len(matrix1))

