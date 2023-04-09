# ЗАДАЧА 1. вводится два числа, опеределить большее из них. числа вводим с терминала

""" a1 = int(input("Type the first num: "))
a2 = int(input("Type the second num: "))

if a1 > a2:
    print(f"The biggest number is {a1}")
elif a1 == a2:
    print(f"The numbers {a1} and {a2} are equal")
else:
    print(f"The biggest number is {a2}") """


""" ЗАДАЧА 2. За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами.
Input:
n = 700
m = 750
Output:
2 """

n = int(input())
m = int(input())
s = (m + n - 1) // n
print(s)

""" Задача №3. Решение в группах
В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32 """

class_a = 20
class_b = 21
class_c = 22
count_desk_a = class_a // 2 if class_a%2 == 0 else class_a // 2 + 1
count_desk_b = class_b // 2 if class_b%2 == 0 else class_b // 2 + 1
count_desk_c = class_c // 2 if class_c%2 == 0 else class_c // 2 + 1
print(f'Общее кол-во парт будет {count_desk_a + count_desk_b + count_desk_c}')

