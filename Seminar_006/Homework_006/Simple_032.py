# Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


print('------------------------------')
print('variant 1')
s = int(input('Размер массива: '))
v_form = int(input('Значения от: '))
v_to = int(input('Значения до: '))
mn = int(input('Искать в диапозоне от: '))
mx = int(input('Искать в диапозоне до: '))
import random as r
lst = [r.randint(v_form, v_to) for _ in range(s)]
print(lst)

for i in range(s):
    if mn <= lst[i] <= mx:
        print(i, end = ' ')





print('------------------------------')
print('variant 2')
a = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
mn = int(input())
mx = int(input())
print(b := [i for i in range(len(a)) if mn <= a[i] and a[i] <= mx])


# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     f min_number <= list_1[i] <= max_number:
#     print(i)