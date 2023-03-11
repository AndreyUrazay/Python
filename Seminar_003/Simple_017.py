# Дан список чисел. Определите, сколько 
# в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить 
# значения списка или список задан изначально.

a = [1, 1, 2, 3, 4, 5, 5, 6, 7, 0]
b = set(a)
print(len(b))

lst = []
length = int(input('Введите длину массива: '))
for i in range(length):
    n = int(input(f'введите элемент {i +1}: '))
    lst.append(n)
print(*lst)

new_lst = []
count = 0 
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
        count += 1

print(count)

