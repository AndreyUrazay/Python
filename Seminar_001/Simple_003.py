# В некоторой школе решили набрать три новых математических класса и 
# оборудовать кабинеты для них новыми партами. За каждой партой
# может сидеть два учащихся. Известно количество учащихся в 
# каждом из трех классов. Выведите наименьшее число парт, 
# которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

a = int (input ("Введите количество учеников в 1-ом классе: "))
b = int (input ("Введите количество учеников в 2-ом классе: "))
c = int (input ("Введите количество учеников в 3-tм классе: "))

a_1 = a // 2 + a%2
b_1 = b // 2 + b%2
c_1 = c // 2 + c%2

table = (a_1 + b_1 + c_1)

print (a_1)
print (b_1)
print (c_1)
print (table)

import math

table_2 = math.ceil((a+b+c)/2)
print (table_2)