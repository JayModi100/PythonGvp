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

    if(len(matrix1) != len(matrix2)):
        return "Error"
    # matrix initialization
    matrix = []
    for row in range(len(matrix1)):
        matrix.append([])
        for col in range(len(matrix1[row])):
            matrix[row].append(matrix1[row][col]+matrix2[row][col])
    return matrix


def multiplicationOfMatrix(matrix1,matrix2):
    rows_A, cols_A = len(matrix1), len(matrix1[0])
    rows_B, cols_B = len(matrix2), len(matrix2[0])

    if cols_A != rows_B:
        return ("Incompatible dimensions for matrix multiplication.")

    result = []
    for i in range(rows_A):
        result.append([])
        for j in range(cols_B):
            p=0
            for k in range(cols_A):
                p += matrix1[i][k] * matrix2[k][j]
            result[i].append(p)
            

    return result
