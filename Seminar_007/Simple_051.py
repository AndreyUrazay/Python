# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, 
# и возвращают True, если это так. Если значение характеристики для 
# разных объектов отличается - то False. Для пустого набора объектов, 
# функция должна возвращать True. Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.
# Ввод: 
# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
# Вывод:
# same

# вариант 1
print('------------------------')
print('variant 1')

def same_by(func, values):
    for i in range(1, len(values)):
        if func(values[i] != func(values[i - 1])):
            return False
        return True

values = [1, 3, 1, 7] 
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')


# вариант 2
print('------------------------')
print('variant 2')

values = [1, 3, 1, 7]

def same_by(func, lst):
    return (res := len(list(map(func, lst)))) == 0 or res == len(lst)

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')


# вариант 3
print('------------------------')
print('variant 3')

values = [1, 3, 1, 7]

def same_by(func, lst):
    return (len(set(map(func, lst)))) == 1

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
