# Задача №33.
# Решение в группах Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот:
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


import random
n = (int(input("Введите количество: ")))
grades = [random.randint(1, 5)for _ in range(n)]
print(grades)

minimum = min(grades)
maximum = max(grades)
print(list(enumerate(grades)))
for i, value in enumerate(grades):
    if value == maximum:
        grades[i] = minimum

print(*grades)