# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, 
# K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# Примечание: Пользователь может вводить значения списка 
# или список задан изначально.


a = [1, 2, 3, 4, 5, 6]
b = [0] * len(a)
k = 3 % len(a)

for i in range(len(a)):
    b[i] = a[i - k]

print(a)
print(b)


ilist = [1, 2, 3, 4, 5, 6, 7, 8]
ilist2 = ilist[-3:] + ilist[:-3]
print(f'{ilist} ==> {ilist2}')


import random

N = 10

lst = [random.randrange(10) for _ in range(N)]
print(f'{lst = }')

k = int(input('k = '))
for _ in range(k):
    lst.insert(0, lst.pop())

print(f'{lst = }')