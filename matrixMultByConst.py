# First input is dimensions eg 2x2 '2 2'
# second is the matrix, each line eg '2 2'
#                                    '2 2'
# third input is the multiplication constant eg 3
# output is the multiplication of const x matrix


# Inputs
a, b = input().split()
a = int(a)
b = int(b)
matrix1 = [list(map(int, input().split())) for _ in range(int(a))]
constant = int(input())
# Calculation
nestedNew = [[y * constant for y in x] for x in matrix1]
# String formatting
stringify = [[str(y) for y in x] for x in nestedNew]
for i in range(len(stringify)):
    print((' ').join(stringify[i]))