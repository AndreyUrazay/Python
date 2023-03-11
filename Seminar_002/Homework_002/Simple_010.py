# Задача 10.
# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное
#  число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной 
# и той же стороной. Выведите минимальное 
# количество монет, которые нужно перевернуть


import random
gerb = 0
resh = 0
i = 0
while i<10:
    i += 1
    coin = random.randint(1,2)
    if coin == 1:
        gerb += 1
    if coin == 2:
        resh += 1
print ("Решек", resh)
print ("Гербов", gerb)

if gerb <= resh:
    print (f"Необходимо перевернуть {gerb} монет, чтобы все были решкой вверх")
else:
    print (f"Необходимо перевернуть {resh} монет, чтобы все были гербом вверх")


# from random import randint

# coins = [randint(0, 1) for _ in range(int(input()))]
# print(coins)
# print(min(
#     coins.count(0),
#     coins.count(1)
# ))
