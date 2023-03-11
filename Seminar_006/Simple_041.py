# Задача 41.
# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая в данном массиве 
# определит количество элементов, у которых два соседних и, 
# при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов 
# в массиве Далее записаны N чисел — элементы массива. 
# Массив состоит из целых чисел.

# ввод:
# 5
# 1 2 3 4 5
# вывод: 0

# ввод
# 5
# 1 5 1 5 1
# вывод: 2

# variant 1
print ('---------------------')
print('Variant 1')
import random as ran
n = int(input('Введите длину массива: '))
rand_lst = [ran.randint(1, 10) for _ in range(n)]
print(rand_lst)

count = 0
for k, v in enumerate(rand_lst):
    if k == 0 or k == len(rand_lst) - 1:
        continue
    if rand_lst[k + 1] < v > rand_lst[k - 1]:
        count += 1

print(count)


# variant 2
print ('---------------------')
print('Variant 2')
rand_lst = []
n = int(input('Введите длину списка: '))
for i in range(n):
    rand_lst.append(int(input(f'Введите элемент {i + 1}: ')))

count = 0
for k, v in enumerate(rand_lst):
    if 0 < k < len(rand_lst) - 1:
        if rand_lst[k + 1] < v > rand_lst[k - 1]:
            count += 1
print(rand_lst)
print(count)

# variant 3
print ('---------------------')
print('Variant 3')

from random import randrange

lst = [randrange(0, 10) for _ in range(int(input('Введите размерность массива: ')))]

count_nums = 0

for i in range(2, len(lst)):
    if lst[i] < lst[i - 1] > lst[i - 2]:
        count_nums += 1
print(lst, '--> ', count_nums)


# variant 4
print ('---------------------')
print('Variant 4')
n = int(input("введите разммерность 1 массива: "))
lst = []
for i in range(n):
    lst.append(int(input(f"элемент {i + 1}: ")))
print(lst)
c = 0
for i in range(len(lst[1:])):
    if lst[i-1] < lst[i] > lst[i+1]:
        c += 1
print(c)