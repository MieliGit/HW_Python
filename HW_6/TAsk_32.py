# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

min_number = int(input("Введите минимальное число диапазона: "))
max_number = int(input("Введите максимальное число диапазона: "))
n = int(input("Введите велечину списка: "))

list_1 = [random.randint(-10, 10) for i in range(n)]

print(list_1)

list_2 = []

for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        list_2.append(i)

print (list_2)