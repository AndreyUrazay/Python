# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# variant 1
mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
    set_1.add(i)
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
    set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')


# variant 2
n = int(input("Введите кол-во элементов в 1 списке: "))
m = int(input("Введите кол-во элементов вo 2 списке: "))
A = list()
B = list()
for i in range(n):
    A.append(int(input("Введите элемент 1-го списка №" + str(i +1) + ': ')))
print("---------------")
for i in range(m):
    B.append(int(input("Введите элемент 2-го списка №" + str(i +1) + ': ')))
print("Список 1:", *A)
print("Список 2:", *B)
res = []
for i in A:
    for j in B:
        if i == j and i not in res:
            res.append(A)
print("Резульат:", *sorted(res))


# variant 3
n = int(input("Введите кол-во элементов в 1 списке: "))
m = int(input("Введите кол-во элементов вo 2 списке: "))
print(f"Введите {n} элементов первого множества")
a_lst = [int(input()) for _ in range(n)]  #a = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
print(f"Введите {m} элементов вторго множества")
b_lst = [int(input()) for _ in range(m)]  # b = [3, 6, 9, 12, 15, 18]
print(*a_lst)
print(*b_lst)
a_set = set(a_lst) # из списка в о множества
b_set = set(b_lst) # из списка в 0 множества
c_set = a_set.intersection(b_set) # Вывод встречающихся чисел
if len(c_set) == 0: # Если нет встречающихся чисел
    print("Числа не встречаются")
else:
    print(sorted(c_set))


