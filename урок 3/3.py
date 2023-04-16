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


""" написать программу для печати всех уник значений в словаре
input [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {"V": "S009"}, {"VIII": "S007"}]
output: {'S005', 'S002', 'S007', 'S001', 'S009', ' S005 '} """

dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {"V": "S009"}, {"VIII": "S007"}]
mnozh = set()
for i in dictionary:
    mnozh.add(list(i.values())[0])
print(mnozh)

dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {"V": "S009"}, {"VIII": "S007"}]
result_set = set()
for i in dict:
    for j in i:
        result_set.add(i[j])

print(result_set)


""" дан массив из целых чисел. подсчитать кол-во элементов массива, больших предыдущего (элемента с предыдущим номером)
[0, -1, 5, 2, 3]
2(-1 < 5, 2 < 3) """

import random
n = int(input("Type the number of the elements: "))
nums = []
count = 0
nums.append(random.randint(-10, 10))

for i in range(n-1):
    nums.append(random.randint(-10, 10))
    if nums[i+1] > nums[i]:
        count += 1

print(nums)
print(f"The number is {count}")