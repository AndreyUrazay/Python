#Рекурсия - это функция, которая вызывает сама себя.
# Пользователь вводит число n. Необходимо вывести n-первых членов последовательности Фибоначи.

def fib(n):
    if n in [1,2]:
        return 1
    return fib(n - 1) + fib(n - 2)

lst_1 = []
for i in range(1, 10):
    lst_1.append(fib(i))
print(lst_1)
