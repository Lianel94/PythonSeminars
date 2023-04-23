""" Задача No31. Общее обсуждение
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
Input: 7 Output: 21 """

n = int(input("Type the number: "))
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(n))



# Задача 29. Найти факториал числа
n = int(input("Type the number: "))
def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n-1)

print(factorial(n)) 


""" Задача No35. Решение в группах
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
Input: 5 Output: yes """

n = int(input("Type the number: "))

def is_simple(n, t = None):
    if t is None:
        t = n - 1
    while t >= 2:
        if n % t == 0:
            return False
        else:
            return is_simple(n, t - 1)
    else:
        return True

print(is_simple(n))


""" Задача 37. Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
Input: 2 -> 3 4 Output: 4 3 """

def sequence(n):
    if n == 0:
        return "+"
    i = input("Type the number: ")
    return sequence(n-1) + i

print(sequence(5))
