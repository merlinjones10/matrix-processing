# Take in a matrix and ''transpose/rotate? it'
# i.e make columns rows
# 1 2 3     1 4 7
# 4 5 6 --> 2 5 8
# 7 8 9     3 6 9

# get the 1st item of every ROW, i.e array, push to new array
#      '' 2nd
# Loop through an array of array with a counter, fetch the nth index of the item


arr = [[1, 2],
       [4, 5],
       [7, 8],
       [8, 5]]



def transpose_matrix(matrix):
    new_matrix = []
    for index in range(len(list[0])):
        new_sub_list = []
        for sub_index in range(len(list)):
            new_sub_list.append(list[sub_index][index])
            if sub_index == len(list) - 1:
                new_list.append(new_sub_list)
    return new_matrix











# create an array, push items to that array
# # wipe the array clean
# test_list = []
# nested_list = []
# for i in range(3):
#    nested_list.append(i)
#
# test_list.append(nested_list)
# print(test_list)