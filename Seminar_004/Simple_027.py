# Задача No27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# variant 1
str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
str = set(str.upper().split())
# str = set(str.split())
# print(type(lst))
print(len(str))


# variant 2
inpt = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

inpt2 = " "

for char in inpt:
    if char == " " or char.isalpha(): #isalpha проверяет буквы
        inpt2 += char

dct = {}

for word in inpt2.lower().split():
    dct[word] = " "

print(len(dct))
