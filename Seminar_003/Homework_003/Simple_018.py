# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
N = int(input(f'Введите длину массива: '))
X = int(input(f'Какое число ищем в массиве? - '))

list = [random.randrange(100) for _ in range(N)] # 1, 2, 3, 4, 5
print(f'{list = }')


number=[abs(list[i]-X) for i in range(len(list))]
print(f'Близкое значение в массиве {list[number.index(min(number))]}')


# variant 2 через словарь
from random import randint
n = int(input("n = "))
lst = [randint(1, n) for _ in range(n)]
print(lst)
x = int(input('x = '))

# dct = {abs(x - item): item for item in list}
# print(type(dct))
# print(dct)
# print(dct[min(dct)])

print(min(lst, key=lambda i: abs(i - x))) #анонимная функция lambda

def func(i):
    return abs(i -x)
print(min(lst, key = func))


