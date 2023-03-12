# append сокр a открытие для добавления данных
# read сокр r открытие для чтения данных
# write сокр w открытие для записи данных
# w+
# r+

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') #здесь указывается режим, в котором будем работать
data.writelines(colors)      # разделителей не будет
data.close()

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
print(56)


peath = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()