# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random

n =  int(input("Введите колличество чисел в первом ряду: "))
m =  int(input("Введите колличество чисел во втором ряду: "))


list_1 = [random.randint(1, 10) for i in range (n)]
list_2 = [random.randint(1, 10) for i in range (m)]

print(list_1)
print(list_2)

list_3 = set(list_1)
list_4 = set(list_2)

list_5 = list_3.union(list_4)

print(f"Уникальный возрастающий ряд чисел = {list_5}")
