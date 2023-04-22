""" Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
Output: 13 """

statement = "She sells sea shells on the sea shore.The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
array1 = statement.lower().replace(".", " ").split(" ")
print(array1)
array = []

for i in array1:
    if i not in array:
        array.append(i)

print(array)
print(len(array))


""" Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию .split() """

string = "a a a b c a a d c d d".split()

for i in range(len(string)):
    print(f"{string[i]}_{string[0:i].count(string[i])}" if string[0:i].count(
        string[i]) != 0 else string[i], end=" ")


""" stroka = input().split()
result = {}
for i in stroka:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
    else:
        print(i, end=' ')
result[i] = result.get(i, 0) + 1 """
