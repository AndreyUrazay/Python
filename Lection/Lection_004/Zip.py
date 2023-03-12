#  zip() применятеся к набору итерируемых объектов и возвращает 
# итератор с кортежами из элементов входных данных

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)

salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data)

# пробегает по минимальному входящему набору 


# enumerate применяет е итериремому объекту и возвращает новый 
# итератор с кортежами из индекса и элеметов входных данных

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data)
