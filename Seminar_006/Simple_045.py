# Задача 45.
# Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) 
# равна числу m и наоборот. Например, 220 и 284 – дружественные числа. 
# По данному числу k выведите все пары дружественных чисел, каждое 
# из которых не превосходит k. Программа получает на вход одно 
# натуральное число k, не превосходящее 105. Программа должна вывести
# все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз 
# (перестановка чисел новую пару не дает).

# ввод 300
# вывод 220   284

# метод Эйлера

print('----------------------------------')
print("метод Эйлера")

s1 = 0
s2 = 0
k = int(input())
for i in range(1, k):
    s1 = 0
    for s in range(1, i // 2 + 1):
        if i % s == 0:
            s1 += s
    if i == s1:
        continue
    s2 = 0
    for j in range(1, s1 // 2 + 1):
        if s1 % j == 0:
            s2 += j
    if s2 == i and i < s1:
        
        print(i, s1)



print('----------------------------------')
print('variant 2')
k = int(input())


for n in range(2, k):
    summ_2 = 0
    for t in range(1, n // 2 + 1):
        if n % t == 0:
            summ_2 += t
    for m in range(n + 1, k + 1):
        summ_1 = 0
        for s in range(1, m // 2 + 1):
            if m % s == 0:
                summ_1 += s
        if n == summ_1 and m == summ_2:
            print(n, m)


print('----------------------------------')
print('variant 3')
c = dict()
d = int(input())

def func(a, b = 0):
    for i in range(1, a):
        if a % i == 0:
            b += i
    return b

for i in range(d):
    if func(i) == func(func(func(i))) and func(i) != func(func(i)) and func(func(i)) not in c:
        c[func(i)] = func(func(i))

print(c)