import operator
# Take in a matrix and 'transpose' it
# i.e make columns rows
# 1 2 3     1 4 7
# 4 5 6 --> 2 5 8
# 7 8 9     3 6 9



def transpose_matrix(matrix):
    new_matrix = []
    for index in range(len(matrix[0])):
        new_sub_list = []
        for sub_index in range(len(matrix)):
            new_sub_list.append(matrix[sub_index][index])
            if sub_index == len(matrix) - 1:
                new_matrix.append(new_sub_list)
    return new_matrix

def add_matrix(m1, m2, operand=operator.add):
    result_matrix = m1.copy()
    for x in range(len(m1)):
        for y in range(len(m1[x])):
            result_matrix[x][y] = operand(m1[x][y], m2[x][y])
    return result_matrix

# transposed = transpose_matrix(matrix2)

# new_array = add_matrix(matrix1, matrix2)

matrix1 = [[1, 2],
           [3, 4]]
matrix2 = [[9, 8],
           [7, 6]]

matrix_mult = []
def mult_matrix(m1, m2):
    for x in range(len(m1)):
        print('')
        for y in range(len(m1[x])):
            # print(f'{m1[x][y]}*{m2[x][y]}')
            print(f'{x} {y}, {} {}')


mult_matrix(matrix1, matrix2)








