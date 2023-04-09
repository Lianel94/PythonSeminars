# задвча. вводится два числа, опеределить большее из них. числа вводим с терминала

a1 = int(input("Type the first num: "))
a2 = int(input("Type the second num: "))

if a1 > a2:
    print(f"The biggest number is {a1}")
elif a1 == a2:
    print(f"The numbers {a1} and {a2} are equal")
else:
    print(f"The biggest number is {a2}")
