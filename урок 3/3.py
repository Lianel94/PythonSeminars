""" дан список [1,1,2,0,-1,3,4,4], output - 6. сколько в нем встречается различных чисел """

""" list_a = [1, 1, 2, 0, -1, 3, 4, 4, 7, 7, 8]
list_to_mnozh = set(list_a)
list_a = list(list_to_mnozh)
print(len(list_a)) """

array = [1, 1, 2, 0, -1, 3, 4, 4]
array2 = []

for i in array:
    if i not in array2:
        array2.append(i)

print(len(array2))




""" дана последовательность из n целых чисел и число k. необходимо сдвинуть всю пос-ть (сдвиг - циклический) на k элементов вправо. k - + число 
input [1,2,3,4,5] k = 2
output [4,5,1,2,3]"""

list_b = [1, 2, 3, 4, 5]
k = 2
for i in range(k):
    list_b.insert(0, list_b.pop(len(list_b) - 1))
print(list_b)
