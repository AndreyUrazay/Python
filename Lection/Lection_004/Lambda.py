def calk2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

# def calk1(a, b):
#     return a + b

# calk1 = lambda a, b: a + b


math(lambda a, b: a + b, 5, 45)

# В списке хранятся числа. Нужно выбрать только четные числа и составить список пар  (число; квадрат числа).
# Пример: 1, 2, 3, 5, 8, 15, 23, 38
# получить [(2, 4), (8, 64), (38, 1444) ]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = list()

for i in data:
    if i % 2 == 0:
        res.append((i, i**2))

print(res)


def select(f, col):
    return [f(x) for x in col]

def wh(f, col):
    return (x for x in col if f(x))
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = wh(lambda x: x % 2 == 0, res)
print(res)
res = select(lambda x: (x, x**2), res)
print(res)



# другой пример
list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x +10, list_1))
print(list_1)


# с клавиатуры вводится некий набор чисел, в качестве раздилителя
# используется пробел. Этот набор чисел будет считан в качестве строки.
# как превраить list строк в list чисел

data = '15 12 2 23 45 56'
print(data)

# data = data.split()
# print(data)

data = list(map(int, data.split()))
print(data)


def wh(f, col):
    return (x for x in col if f(x))
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
print(res)
res = wh(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)



# фильтрует значения

data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)


data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)
