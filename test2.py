#9 Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше
# другого).

print('Программа находит среднее число из 3х введенных.')

number_list = []

number_list.append(int(input('Введите число 1: ')))
number_list.append(int(input('Введите число 2: ')))
number_list.append(int(input('Введите число 3: ')))

number_list.remove(max(number_list))

print(f'Среднее число: {max(number_list)}')