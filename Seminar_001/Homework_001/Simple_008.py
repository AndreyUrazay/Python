# Задача 8: 
# Требуется определить, можно ли от шоколадки 
# размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по 
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n= input("Сколько 'столбиков' в шоколадке: ")
n = int(n)

m= input("Сколько 'строчек' в шоколадке: ")
m = int(m)

k = input("Сколько долек Вы хотите отломить: ")
k = int(k)

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print(f"От шоколадки размером {n} х {m} можно отломить {k} долек(и)")
else:
    print("Дольку никак не отломить. P.s. ешь в тихушку")