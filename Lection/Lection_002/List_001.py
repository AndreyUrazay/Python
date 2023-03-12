list_1 = []
lis_1 = list()
list_1 = [1, 2, 3, 8]

print ("пример 1")
print(list_1)

print ("пример 2")
print(*list_1)

print ("пример 3")
for i in list_1:
    print (i)

print ("пример 4")
print(len(list_1))

print ("пример 5")
print(list_1[2])

print ("пример 6")
list_1 = [1, 5]
print(list_1)
list_1.append(8)
print(list_1)
list_1.append(85)
print(list_1)

print ("пример 7")
list_1 = []
print(list_1)
for i in range(5):
    list_1.append(i)
    print(list_1)

  
print("Удаление последнего элемента списка")
list_1 = [12, 7, -1, 21, 0] 
print (list_1.pop()) # 0

a = list_1.pop()
print(a) #0 удаляет последний и возращает


print ("Удаление конкретного элемента из списка")
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0)) #12
print(list_1) # [7, -1, 21, 0]

print ("Добавление элемента на нужную позицию")
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11))
print(list_1)