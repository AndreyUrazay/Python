# Задача 31.
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21   через индекс будет 13

# Задание необходимо решать через рекурсию

# считаем через индекс

# variant 1
def fibo(n):

    if n in [0, 1]:
        return n
    return fibo(n-1)+fibo(n-2)


print(fibo(int(input())))


# variant 2
def fib(N): return N if N in (0, 1) else fib(N-1) + fib(N-2)

print(fib(7))
