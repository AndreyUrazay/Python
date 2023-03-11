# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю 
# историю наблюдений за погодой. Они обратились к синоптикам, 
# а те, в свою очередь, занялись исследованиями статистики 
# за прошлые годы. Их интересует, сколько дней длилась 
# самая длинная оттепель. Оттепелью они называют период, 
# в который среднесуточная температура ежедневно 
# превышала 0 градусов Цельсия. Напишите программу, 
# помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых 
# дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
#  Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2


print('Variant_1')
a = int(input('Введите количество дней: '))
temp = 0 
max_ = 0

for i in range (a):
    t = int(input("Введите среднесуточную температуру: "))
    if t > 0:
        temp += 1
        if max_ < temp:
            max_ = temp
    else:
        temp = 0

print(f"Самая длинная оттепель длилалась {max_} дней")

print ('Variant 2')

a_2 = int(input('Введите количество дней: '))
temp_2 = 0 
max_2 = 0

for i_2 in range (a_2):
    t_2 = int(input("Введите среднесуточную температуру: "))
    if t_2 > 0:
        temp_2 += 1            
    else:
        temp_2 = 0
        continue
    max_2 = temp_2
print(f"Самая длинная оттепель длилалась {max_2} дней")