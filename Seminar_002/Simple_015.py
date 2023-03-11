# Иван Васильевич пришел на рынок и решил купить два арбуза: 
# один для себя, а другой для тещи. Понятно, что для себя нужно 
# выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: 
# арбузов слишком много и он не знает как же выбрать 
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# ves_arbuzov = [5, 1, 6, 5, 9]
# sor_ted = sorted(ves_arbuzov)
# print(sor_ted[0], sor_ted[-1])

print('Variant 1')
n = int(input("Введите число арбузов: "))

ligth = 0
heavy = 0

for i in range(n):
    weight = int(input(f'Вес арбуза №{i +1}:'))
    if weight > heavy:
        heavy = weight
    elif ligth == 0 or weight < ligth:
        ligth = weight

print(f'Самый легкий арбуз: {ligth}, самый тяжелый арбуз: {heavy}')


print('variant 2')
n = int(input("Введите число арбузов: "))

heavy = 0

import math
ligth = math.inf

for i in range(n):
    weight = int(input(f'Вес арбуза №{i +1}:'))
    if weight > heavy:
        heavy = weight
    if weight < ligth:
        ligth = weight

print(f'Самый легкий арбуз: {ligth}, самый тяжелый арбуз: {heavy}')

print('variant 3')
quantity = int(input('Введите число арбузов: '))

for i in range(quantity):
    weight = int(input(f'Вес арбуза №{i +1}:'))
    if i == 0:
        light = weight
        heavy = weight
    elif weight < light:
        light = weight
    if weight > heavy:
        heavy = weight

print(f'Самый легкий арбуз: {light}, самый тяжелый арбуз: {heavy}')



print('variant 4')
num = int(input('Введите общее количество арбузов: '))
a = [int(input()) for i in range(num)]
print('----------------')
print(f'для тещи арбуз {min(a)} кг, для себя {max(a)} кг')