# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[1..N]. Пользователь 
# в первой строке вводит натуральное число 
# N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1


import random
N = int(input(f'Введите длину массива: '))
X = int(input(f'Какое число ищем в массиве? - '))

list = [random.randrange(5) for _ in range(N)] # 1, 2, 3, 4, 5
print(f'{list = }')

print(list.count(X))