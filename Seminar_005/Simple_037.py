# Зададача 37.
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы
# и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


def rev(n):

    if n == 0:
        return
    else:
        x = (int(input("Введите число: ")))
        rev(n-1)
        print(f'Обратная последовательность чисел {x}')

n = int(input("Введите количество чисел: "))
rev(n)
