# 1 0 17
# 15 19 7
#
# 5 6 78 9
# 29 31 47 1
# 14 17 0 3

# =
# 243  295	 78	   60
# 724  798	 2063  175


def transpose_matrix(matrix):
    new_matrix = []
    for index in range(len(matrix[0])):
        new_sub_list = []
        for sub_index in range(len(matrix)):
            new_sub_list.append(matrix[sub_index][index])
            if sub_index == len(matrix) - 1:
                new_matrix.append(new_sub_list)
    return new_matrix
list1 = [[1, 0 , 17],
         [15,19, 7],
         ]
list2Reg =[[5 , 6 , 78, 9],
           [29, 31, 47, 1],
           [14, 17, 0 , 3]]

# t 4 x 3
list2 = transpose_matrix(list2Reg)
nested = []
listFinal = []
dot_sum = 0
# COLS
for _ in range(len(list1)):
    for i in range(len(list2)):
    # ROWS
        for x in range(len(list2[0])):
            dot_sum += list1[_][x] * list2[i][x]
            if x == len(list1[0]) - 1:
                nested.append(dot_sum)
                dot_sum = 0
            if x == len(list1[0]) - 1 and i == len(list2) - 1:
                listFinal.append(nested)
                nested = []




print(listFinal)
