# Задача No29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
# n = int(input())
# if max_number < n:
# n = max_number
# print(n)

# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
# n = int(input())
# if max_number > n:
# max_number = n
# print(max_number)


# variant 1
import random
n= 20

a = [random.randint(1, 10) for _ in range(n)]
print(a)
b = []

idx = random.randrange(len(a))

a.insert(idx, 0)

for i in range(len(a)):
    if a[i] != 0:
        b.append(a[i])
    else:
        break
print(b)
print(max(b))


# variant 2
import random 
lst = []
while True:
    i = random.randrange(11)
    lst.append(i)
    if i == 0:

        break

print(lst)
print(max(lst))


# variant 3

import random
lst = []
while (i := random.randrange(11))!= 0:
    lst.append(i)

lst.append(i)

print(lst)
print(max(lst)) 