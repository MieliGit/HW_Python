# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def multi1(a, b):
    a *= x
    b -= 1
    if b > 1:
        return multi1(a, b)
    return a

n = x = int(input("Введите число, которое хотите возвести в степень: "))

m = int(input("Введите степень: "))

print(multi1(n,m))