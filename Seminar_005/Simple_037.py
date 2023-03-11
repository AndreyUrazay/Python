# Зададача 37.
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы
# и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# variant 1
def rev(n):

    if n == 0:
        return
    else:
        x = (int(input("Введите число: ")))
        rev(n-1)
        print(f'Обратная последовательность чисел {x}')


n = int(input("Введите количество чисел: "))
rev(n)

# variant 2
n = int(input())


def rec(n):

    if n == 0:
        return
    i = int(input())
    rec(n - 1)
    print(i, end=' ')


rec(n)


# variant 3

from random import randrange

def func(n):
    if n == 0:
        return ' -> '
    
    var = randrange(n)
    print(var, end=' ')
    return f'{func(n -1)} {var}'

print(func(5))
