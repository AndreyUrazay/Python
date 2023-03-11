# Напишите программу для печати всех уникальных значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# Примечание: Список словарей задан изначально. Пользователь его не вводит


lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

lst2 = []

# множеством
for dct in lst:
    for i in dct:
        lst2.append(dct[i])
        
print(set(lst2))

#списком
for dct in lst:
    for i in dct:
        if lst2.count(dct[i]) == 0:
            lst2.append(dct[i])
        
print(set(lst2))


lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
unique = set()

for element in lst:
    for values in element.values():
        unique.add(*element.values())
print(lst)
print(unique)

