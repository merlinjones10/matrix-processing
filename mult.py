# Multiply matrices (2nd already transposed)
# multiply the nth elements in an array together

list1 = [[1, 5],
         [0, 3],
         [1, 5]]
list2 = [[4, 3],
         [2, 1],
         [5, 3]]
nested = []
listFinal = []
dot_sum = 0
def transpose_matrix(matrix):
    new_matrix = []
    for index in range(len(matrix[0])):
        new_sub_list = []
        for sub_index in range(len(matrix)):
            new_sub_list.append(matrix[sub_index][index])
            if sub_index == len(matrix) - 1:
                new_matrix.append(new_sub_list)
    return new_matrix


for _ in range(len(list1)):
    for i in range(len(list1)):
        for x in range(len(list1[0])):
            dot_sum += list1[_][x] * list2[i][x]
            if x == len(list1[0]) - 1:
                nested.append(dot_sum)
                dot_sum = 0
            if x == len(list1[0]) - 1 and i == len(list1) - 1:
                listFinal.append(nested)
                nested = []




print(listFinal)
