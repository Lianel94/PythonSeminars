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