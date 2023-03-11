# Дано натуральное число. Требуется определить, 
# является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, 
# иначе выведите NO. Напомним, что в соответствии 
# с григорианским календарем, год является високосным, 
# если его номер кратен 4, но не кратен 100, 
# а также если он кратен 400.
# Input: 2016
# Output: YES

y = int (input ("Введите год для определения високосности: "))
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print (f"Введенный год {y} явлется високосным")
else:
    print (f"Введенный {y} год является не високосным")

print ('Високосный' if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else 'Не високосный') #вариант 2
print (y % 4 == 0 and y % 100 != 0 or y % 400 == 0) #вариант 3