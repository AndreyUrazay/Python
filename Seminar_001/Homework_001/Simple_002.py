# Задача 2: 
# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


# a = int (input ("Введите 1-е число:"))
# b = int (input ("Введите 2-е число:"))
# c = int (input ("Введите 3-е число:"))

# summ = a + b + c 

# print (f"Сумма 3-х чисел = {summ}")


z = input ("Вариант 1. Введите 3-х значное число: ")
z_1 = int (z[0])
z_2 = int (z[1])
z_3 = int (z[2])

summ_1 = z_1 + z_2 + z_3
print (f"Вариант 1. Сумма чисел 3х значного числа равна = {summ_1}")


n = input("Вариант 2. Введите трехзначное число: ")
n = int(n)
 
d1 = n % 10
d2 = n % 100 // 10
d3 = n // 100
 
print("Вариант 2. Сумма цифр числа:", d1 + d2 + d3)


m = input("Вариант 3. Введите трехзначное число: ")
m = int(m)
 
m1 = m % 10
m = m // 10
m2 = m % 10
m = m // 10
 
print("Вариант 3. Сумма цифр введенного числа:", m + m1 + m2)


# def sum_digit(num):
#     return num // 100 + num //10 % 10 + num % 10

#     if __name__ == "__main__":
#         print(sum_digit(int(input)))
