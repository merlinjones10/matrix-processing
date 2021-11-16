# Inputs
a, b = input('x and y M1: ').split()
a = int(a)
b = int(b)
matrix1 = [list(map(int, input('Matrix 1: ').split())) for _ in range(int(a))]
c, d = input('x and y M2: ').split()
c = int(c)
d = int(d)
matrix2 = [list(map(int, input('Matrix 2: ').split())) for _ in range(int(c))]

# Calculation, modify existing copy rather than creating new nested lists
if a == c and b == d:
    sum = matrix1.copy()
    for x in range(len(matrix1)):
        for y in range(len(matrix1[x])):
            sum[x][y] = (matrix1[x][y] + matrix2[x][y])
    # String formatting and printing
    stringify = [[str(y) for y in x] for x in sum]
    for i in range(len(stringify)):
        print((' ').join(stringify[i]))
else:
    print('ERROR, matrices need to be the same size')

# Another solution copied from hyperskill:
# def matrix_add(x_matrix, y_matrix):
#     z_matrix = []
#     for i in range(len(x_matrix)):
#         row_ = [x_matrix[i][j] + y_matrix[i][j] for j in range(len(x_matrix[i]))]
#         z_matrix.append(row_)
#     return z_matrix