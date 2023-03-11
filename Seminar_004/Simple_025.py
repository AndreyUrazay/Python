# Задача No25. 
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# вариант 1
a = input("Введите слово: ").split()
b = []

for i in range(len(a)):
    if a[i] in b:
        b.append(a[i] + '_' + str(a[:i].count(a[i])))
    else:
        b.append(a[i])

print(*b)

# вариант 2
st = "a a a b c a a d c d d"
lt = st.split()
print(lt)
dct = {}
output = " "
for i in lt:
    if i in dct:
        dct[i] += 1
        output += f"{i}_{dct[i]}"
    else:
        dct[i] = 0 
        output += f"{i}  "

print(dct)
print(output)
