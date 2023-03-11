# Задача 28:
# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4


# variant 1
print("Вариант 1")
def sum(a, b):
    if b == 0:
        return a
    return sum(a+1, b-1)


a = int(input("Введите число А = "))
b = int(input("Введите числов B = "))

print(f'Сумма чисел {a} и {b} равна {sum(a, b)}')

# variant 2
print("-----------------------------")
print("Вариант 2")
def sum(a,b):
    if a<b:
        a,b = b,a
    if b==0:
        return a
    elif a==0:
        return b
    else:
        return sum(a+1,b-1)
    
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(f'Сумма чисел {a} и {b} равна {sum(a, b)}')


# variant 3
print("-----------------------------")
print("Вариант 3")
import random
a = int(random.randrange(0, 100))
b = int(random.randrange(0, 100))
print(f'Первое число = {a}, второе число = {b}')


def sum(a, b):
    if a != 0:
        a = a - 1
        return 1 + sum(a, b)
    if b != 0:
        b = b - 1
        return 1+sum(a, b)
    if a == 0 and b == 0:
        return 0


print(f'Сумма чисел {a} и {b} равна {sum(a, b)}')


# variant 4
print("-----------------------------")
print("Вариант 4")
def sum(a, b):
    if b == -1:
        return 0
    return a + sum(1, b - 1)


print(
    f"Сумма чисел = {sum(int(input('Введите первое число: ')), int(input('Введите второе число: ')))}")
