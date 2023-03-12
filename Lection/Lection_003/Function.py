# функция. пример 1
def sum_numbers(n, y = 'Hello'):
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa
    print('stop')

a = sum_numbers(5, 'qwrty')
print(a)

# функция принимающая неограниченное количество аргументов
def sum_str(*args):
    res = ''
    for i in args:
        res += i 
    return res

print(sum_str('q', 'e', 'l'))
print(sum_str('q', 'e', 'l', 'r', 'f'))
