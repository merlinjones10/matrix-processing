# Multiply matrices (2nd already transposed)
# multiply the nth elements in an array together

list1 = [[1, 5],
         [0, 3]]
list2 = [[4, 3],
         [2, 1]]
nested = []
listFinal = []
mySum = 0

for _ in range(len(list1)):

    for i in range(len(list1)):

        for x in range(len(list1)):
            print(_, i, x)
            mySum += list1[_][x] * list2[i][x]
            print(list1[_][x] * list2[i][x])
            if x == 1:
                nested.append(mySum)
                mySum = 0
            if x == 1 and i == 1:
                listFinal.append(nested)
                nested = []




print(listFinal)