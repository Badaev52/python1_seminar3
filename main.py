# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random
from math import sqrt

print("Задача 16")
n = int(input("Задайте количество элементов массива: "))
list_1 = list()
for i in range(n):
    list_1.append(random.randrange(0,10))

print(list_1)

x = int(input("Задайте число: "))

col = 0
for i in list_1:
    if i == x:
        col += 1

print(f"-> {col}")