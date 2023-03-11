# Задача 39.
# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), 
# которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, 
# затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива
# Ввод: 
# 7 
# # 3 1 3 4 2 4 12
# Вывод:
# 3 3 2 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)


# variant 1
print("Variant 1")
n = int(input("введите разммерность 1 массива: "))
mass1 = []
mass2 = []
for i in range(n):
    mass1.append(int(input(f"элемент {i + 1}: ")))

m = int(input("введите разммерность 2 массива: "))
for i in range(m):
    mass2.append(int(input(f"элемент {i + 1}: ")))


for i in mass1:
    if i not in mass2:
        print(i, end="  ")



# variant 2
print('-------------------------')
print("Variant 2")
lst = []
n = int(input('Введите длину списка: '))
for i in range(n):
    lst.append(int(input(f'Введите элемент {i + 1}: ')))

lst2 = []
m = int(input('Введите длину списка: '))
for i in range(m):
    lst2.append(int(input(f'Введите элемент {i + 1}: ')))

res = []
for i in lst:
    if not i in lst2:
        res.append(i)

print(*lst)
print(*lst2)
print(*res)

# variant 3
print('-------------------------')
print("Variant 3")

a = [lst[i] for i in range(n) if not lst[i] in lst2]
print(*a)

