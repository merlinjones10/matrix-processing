# Prints a menu consisting of 4 options. The example shows what the menu should look like.
# Reads the user's choice.
# Reads all data (matrices, constants) needed to perform the chosen operation. The example shows the input format in each case.
# Calculates the result and outputs it. The example shows how your output should look like.
# Repeats all these steps.
import sys
print(sys.version)
promptWords = ['Enter size of first matrix: ', 'Enter size of second matrix: ']
error = 'The operation cannot be performed'
class Size:
    def __init__(self, size):
        self.x = size[0]
        self.y = size[1]

class MatrixAndDims:
    def __init__(self, size, matrix):
        self.size = Size(size)
        self.matrix = matrix

def matrixInput(prompt=f'Enter size of matrix'):
    x, y = input(prompt).split()
    size = (int(x), int(y))
    matrix = [list(map(float, input(f'Enter matrix (row {_ + 1}):  ').split())) for _ in range(int(x))]
    return MatrixAndDims(size, matrix)

def stringifyAndPrint(matrix):
    stringify = [[str(y) for y in x] for x in matrix]
    print('The result is:')
    for i in range(len(stringify)):
        print((' ').join(stringify[i]))

def transpose_matrix(matrix):
    new_matrix = []
    for index in range(len(matrix[0])):
        new_sub_list = []
        for sub_index in range(len(matrix)):
            new_sub_list.append(matrix[sub_index][index])
            if sub_index == len(matrix) - 1:
                new_matrix.append(new_sub_list)
    return new_matrix

def matrixAddition():
    matrix1 = matrixInput(promptWords[0])
    matrix2 = matrixInput(promptWords[1])
    if matrix1.size.x == matrix2.size.x and matrix1.size.y == matrix2.size.y:
        result = matrix1.matrix.copy()
        for x in range(len(matrix1.matrix)):
            for y in range(len(matrix1.matrix[x])):
                result[x][y] = (matrix1.matrix[x][y] + matrix2.matrix[x][y])
        stringifyAndPrint(result)
    else: print(error)

def matrixMultByConst():
    matrix1 = matrixInput(promptWords[0])
    constant = int(input('Multiply by: '))
    nestedNew = [[y * constant for y in x] for x in matrix1.matrix]
    stringifyAndPrint(nestedNew)



def matrixMultiplication():
    matrix1 = matrixInput(promptWords[0])
    matrix2 = matrixInput(promptWords[1])
    matrix2T = transpose_matrix(matrix2.matrix)
    nested = []
    listFinal = []
    dot_sum = 0
    if matrix1.size.y == matrix2.size.x:
        for _ in range(len(matrix1.matrix)):
            for i in range(len(matrix2T)):
                for x in range(len(matrix2T[0])):
                    dot_sum += matrix1.matrix[_][x] * matrix2T[i][x]
                    if x == len(matrix1.matrix[0]) - 1:
                        nested.append(dot_sum)
                        dot_sum = 0
                    if x == len(matrix1.matrix[0]) - 1 and i == len(matrix2T) - 1:
                        listFinal.append(nested)
                        nested = []
        stringifyAndPrint(listFinal)
    else: print(error)

# PROGRAM
programRunning = True
while programRunning:
    chosenOperation = input('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit\nYour choice : ')
    if chosenOperation == '1':
        matrixAddition()
    if chosenOperation == '2':
        matrixMultByConst()
    if chosenOperation == '3':
        matrixMultiplication()
    if chosenOperation == '0':
        programRunning = False





