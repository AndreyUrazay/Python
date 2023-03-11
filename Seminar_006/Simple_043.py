# Задача 43. 
# Дан список чисел. Посчитайте, сколько в нем пар элементов, 
# равных друг другу. Считается, что любые два элемента, 
# равные друг другу образуют одну пару, которую необходимо 
# посчитать. Вводится список чисел. Все числа списка находятся
# на разных строках.

# ввод 1 2 3 2 3
# вывод 2


# variant 1
print('-------------------')
print('Variant 1')

lst = []
n = int(input('Введите длину списка: '))
for i in range(n):
    lst.append(int(input(f'Введите элемент {i + 1}: ')))
print(*lst)

count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if lst[i] == lst[j]:
            count += 1
print(count)


# variant 2
print('-------------------')
print('Variant 2')
from random import randint
# a = [randint(0, 5) for i in range(int(input('Количество элементов массива: ')))]
a = [5, 5, 5, 5, 5, 4, 4, 4, 4, 4]
cnt = 0 
for j in range(len(a)):
    cnt += a[j + 1:].count(a[j])
print(a, cnt)


# variant 3
print('-------------------')
print('Variant 3')

def func(lst: list) -> int:
    el, *lst = lst # el = lst[0], lst = [1:]
    if lst:
        return func(lst) + lst.count(el)

    return 0


if __name__ == '__main__':
    print(func([1, 2, 3, 2, 3]))