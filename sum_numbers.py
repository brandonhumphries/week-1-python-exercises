#Sum the Numbers
numbers = [1, 13, -8, 2, 7, 5]
total = 0
for number in numbers:
    total += number
print total

#Largest Number
x = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > x:
        x = numbers[i]
    else:
        x = x
print x

#Smallest Number
y = numbers[0]
for i in range(len(numbers)):
    if numbers[i] < y:
        y = numbers[i]
    else:
        y = y
print y

#Even Numbers
for number in numbers:
    if number % 2 == 0:
        print number

#Positive Numbers
for number in numbers:
    if number > 0:
        print number

#Positive Numbers 2
positive_numbers = []
for number in numbers:
    if number > 0:
        positive_numbers.append(number)
print positive_numbers

#Multiply a List
factor = 2
multiplied_list = []
for number in numbers:
    multiplied_list.append(number * factor)
print multiplied_list

#Multiply Vectors
list1 = [2, 4, 5]
list2 = [2, 3, 6]
list3 = []
for i in range(len(list1)):
    list3.append(list1[i] * list2[i])
print list3

#Matrix Addition
matrix_list1 = [[1, 3], [2, 4]]
matrix_list2 = [[5, 2], [1, 0]]
matrix_list3 = []
for i in range(len(matrix_list1)):
    ind_list1 = matrix_list1[i]
    ind_list2 = matrix_list2[i]
    ind_list3 = []
    for j in range(len(ind_list1)):
        x = (ind_list1[j] + ind_list2[j])
        ind_list3.append(x)
    matrix_list3.append(ind_list3)
print matrix_list3

m1 = [[1, 3], [2, 4]]
m2 = [[5, 2], [1, 0]]
#r = [[0, 0], [0, 0]]
r = []
for row in m1:
    wip = []
    for col in row:
        wip.append(0)
    r.append(wip)

width = len(r[0])
height = len(r)

for i in range(height):
    for j in range(width):
        r[i][j] = m1[i][j] + m2[i][j]
print r

#Matrix Addition 2
matrix_list1 = [[1, 3, 1], [2, 4, 0], [2, 2, 4]]
matrix_list2 = [[5, 2, 2], [1, 0, 4], [1, 3, 1]]
matrix_list3 = []
for i in range(len(matrix_list1)):
    ind_list1 = matrix_list1[i]
    ind_list2 = matrix_list2[i]
    ind_list3 = []
    for j in range(len(ind_list1)):
        x = (ind_list1[j] + ind_list2[j])
        ind_list3.append(x)
    matrix_list3.append(ind_list3)
print matrix_list3


#De-dup
numbers_list = [1, 8, 2, 3, 3, 8, 9, 4, 3, 1, 5]
new_list = []
for thing in things:
    if thing not in new_list:
        new_list.append(thing)
print new_list


#Matrix Multiplication
