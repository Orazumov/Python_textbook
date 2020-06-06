#magicians = ['alice', 'david', 'carolina']

#for magician in magicians:
#    print(magician)

#for magician in magicians:
#    print(magician.title() + ", that was a great trick!")

#4-1. Пицца: вспомните по крайней мере три ваши любимые разновидности пиццы. Сохраните их в списке и используйте цикл for для вывода всех названий.
#Измените цикл for так, чтобы вместо простого названия пиццы выводилось сообщение, включающее это название. Таким образом, для каждого элемента должна
# выводиться строка с простым текстом вида «I like pepperoni pizza».
#Добавьте в конец программы (после цикла for) строку с завершающим сообщением. Таким образом, вывод должен состоять из трех (и более) строк с названиями
# пиццы и дополнительного сообщения, скажем, «I really love pizza!».

pizzas = ['4 cheeses', 'chicken range', 'margarita']
for pizza in pizzas:
    print(f'\tI like {pizza} pizza.')
print("\nI really love pizza!")

#4-2. Животные: создайте список из трех (и более) животных, обладающих общей характеристикой. Используйте цикл for для вывода названий всех животных.
#Измените программу так, чтобы вместо простого названия выводилось сообщение, включающее это название, например «A dog would make a great pet».
#Добавьте в конец программы строку с описанием общего свойства. Например, можно вывести сообщение «Any of these animals would make a great pet!».

print('*'*50)

pets = ['dog', 'cat', 'rat']

for pet in pets:
    print(f'A {pet} would make a great pet')
print('\nAny of these animals would make a great pet!')

#4-3. Считаем до 20: используйте цикл for для вывода чисел от 1 до 20 включительно.
for i in range(1, 21):
    print(i)

#4-4. Миллион: создайте список чисел от 1 до 1 000 000, затем воспользуйтесь циклом for для вывода чисел. (Если вывод занимает
# слишком много времени, остановите его нажатием Ctrl+C или закройте окно вывода.)
million_list = [i for i in range(1, 1000001)]
#for number in million_list:
#    print(number)

#4-5. Суммирование миллиона чисел: создайте список чисел от 1 до 1 000 000, затем воспользуйтесь функциями min() и max() и
# убедитесь в том, что список действительно начинается с 1 и заканчивается 1 000 000. Вызовите функцию sum() и посмотрите,
# насколько быстро Python сможет просуммировать миллион чисел.
print('min', min(million_list))
print('max', max(million_list))
print('sum', sum(million_list))


#4-6. Нечетные числа: воспользуйтесь третьим аргументом функции range() для создания списка нечетных чисел от 1 до 20. Выведите
# все числа в цикле for.

odd_numbers = [i for i in range(1, 20, 2)]
for number in odd_numbers:
    print(number)

#4-7. Тройки: создайте список чисел, кратных 3, в диапазоне от 3 до 30. Выведите все числа своего списка в цикле for.

three_numbers = [i for i in range(3, 30, 3)]
for number in three_numbers:
    print(number)

#4-8. Кубы: результат возведения числа в третью степень называется кубом. Например, куб 2 записывается в языке Python в виде
# 2**3. Создайте список первых 10 кубов (то есть кубов всех целых чисел от 1 до 10) и выведите значения всех кубов в цикле for.

list_3 = []
for number in range(1, 11):
    list_3.append(number**3)
print(list_3)

#4-9. Генератор кубов: используйте конструкцию генератора списка для создания списка первых 10 кубов.

list_3 = [i**3 for i in range(1, 11)]

print(id(odd_numbers))
print(id(odd_numbers[:]))

#4-10. Срезы: добавьте в конец одной из программ, написанных в этой главе, фрагмент, который делает следующее.
#Выводит сообщение «The first three items in the list are:», а затем использует срез для вывода первых трех элементов из списка.
#Выводит сообщение «Three items from the middle of the list are:», а затем использует срез для вывода первых трех элементов из середины списка.
#Выводит сообщение «The last three items in the list are:», а затем использует срез для вывода последних трех элементов из списка.
print(f'The first three items in the list are:{list_3[:3]}')
middle = int(len(list_3)/2)
print(f'Three items from the middle of the list are:{list_3[middle:middle + 3]}')
print(f'The last three items in the list are:{list_3[-3:]}')

#4-11. Моя пицца, твоя пицца: начните с программы из упражнения 4-1. Создайте копию списка с видами пиццы, присвойте ему имя friend_pizzas.
pizzas = ['4 cheeses', 'chicken range', 'margarita']
friend_pizzas = pizzas[:]

# Затем сделайте следующее.
#Добавьте новую пиццу в исходный список.
#Добавьте другую пиццу в список friend_pizzas.
pizzas.append('la marina')
friend_pizzas.append('vegan')

#Докажите, что в программе существуют два разных списка. Выведите сообщение «My favorite pizzas are:», а затем первый список в цикле for.
# Выведите сообщение «My friend’s favorite pizzas are:», а затем второй список в цикле for. Убедитесь в том, что каждая новая пицца
# находится в соответствующем списке.
print('My favorite pizzas are:')

for i in pizzas:
    print(i)

print('My friend’s favorite pizzas are:')

for i in friend_pizzas:
    print(i)

#4-12. Больше циклов: во всех версиях foods.py из этого раздела мы избегали использования цикла for при выводе для экономии места.
# Выберите версию foods.py и напишите два цикла for для вывода каждого списка.

print('My foods are:')


my_foods = ['pizza', 'falafel', 'carrot cake']

for i in my_foods:
    print(i)



#4-13. Шведский стол: меню «шведского стола» в ресторане состоит всего из пяти пунктов. Придумайте пять простых блюд и сохраните их в кортеже.
#Используйте цикл for для вывода всех блюд, предлагаемых рестораном.
dishes = ('dish1', 'dish2', 'dish3', 'dish4', 'dish5')

for i in dishes:
    print(i)

#Попробуйте изменить один из элементов и убедитесь в том, что Python отказывается вносить изменения.

#dishes[0] = '1'

dishes = ('dish6', 'dish7', 'dish8', 'dish9', 'dish10')

#Ресторан изменяет меню, заменяя два элемента другими блюдами. Добавьте блок кода, который заменяет кортеж, и используйте цикл for для вывода
# каждого элемента обновленного меню.

for i in dishes:
    print(i)

#5-1. Проверка условий: напишите последовательность условий. Выведите описание каждой проверки и ваш прогноз относительно ее результата.
# Код должен выглядеть примерно так:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#Внимательно просмотрите результаты. Убедитесь в том, что вы понимаете, почему результат каждой строки равен True или False.
#Создайте как минимум 10 условий. Не менее 5 должны давать результат True, а не менее 5 других — результат False.

drink = 'water'
print("Is drink == 'wine'? I predict False.")
print(drink == 'wine')
print("\nIs drink == 'borjomi'? I predict False.")
print(drink == 'borjomi')
print("\nIs drink == 'juice'? I predict False.")
print(drink == 'juice')
print("\nIs drink == 'water'? I predict True.")
print(drink == 'water')
print("\nIs drink == 'fresh juice'? I predict False.")
print(drink == 'fresh juice')

#5-2. Больше условий: количество условий не ограничивается 10. Попробуйте написать другие условия и включить их в
# conditional_tests.py. Программа должна выдавать по крайней мере один истинный и один ложный результат для
# следующих видов проверок.

#Проверка равенства и неравенства строк.

print('*'*50)

programming_langauge = 'Python'
print('Is programming langauge C++?')
print(programming_langauge == 'C++')
print('\nIs programming langauge Python?')
print(programming_langauge == 'Python')

#Проверки с использованием функции lower().

print('*'*50)
line = 'This is simple LINE!'

print('Is this like a simple line?')
print(line.lower() == 'this is simple line!')

#Числовые проверки равенства и неравенства, условий «больше», «меньше», «больше или равно», «меньше или равно».

print('*'*50)
age = 19
print('Is age more than 18?')
print(age > 18)
print('\nIs age >= 19?')
print(age >= 19)
print('\nIs age <= 19?')
print(age <= 19)
print('\nIs age == 19?')
print(age == 19)

#Проверки с ключевым словом and и or.

print('*'*50)

my_name = 'Oleg'

print('Is my name Misha or Kostya')
print(my_name == 'Misha' or my_name == 'Kostya')
print('\nIs my name Oleg and starting with capital letter?')
print(my_name == 'Oleg' and my_name[0].isupper())

#Проверка вхождения элемента в список.

print('*'*50)
my_fish = ['ternecii', 'guppi', 'som']
print('Is there som in my aquarium?')
print('som' in my_fish)

#Проверка отсутствия элемента в списке.

print('*'*50)

print('Is there barakuda in my aquarium?')
print('barakuda' in my_fish)


#5-3. Цвета 1: представьте, что в вашей компьютерной игре только что был подбит корабль пришельцев. Создайте переменную с
# именем alien_color и присвойте ей значение ‘green’, ‘yellow’ или ‘red’.
#Напишите команду if для проверки того, что переменная содержит значение ‘green’. Если условие истинно, выведите
# сообщение о том, что игрок только что заработал 5 очков.
#Напишите одну версию программы, в которой условие if выполняется, и другую версию, в которой оно не выполняется.
# (Во второй версии никакое сообщение выводиться не должно.)

print('*'*50)

alien_color = 'green'
if alien_color == 'green':
    print('You have earned 5 scores!')

alien_color = 'red'
if alien_color == 'green':
    print('You have earned 5 scores!')

#5-4. Цвета 2: выберите цвет, как это было сделано в упражнении 5-3, и напишите цепочку if-else.
#Напишите команду if для проверки того, что переменная содержит значение ‘green’. Если условие истинно,
# выведите сообщение о том, что игрок только что заработал 5 очков.
#Если переменная содержит любое другое значение, выведите сообщение о том, что игрок только что заработал 10 очков.
#Напишите одну версию программы, в которой выполняется блок if, и другую версию, в которой выполняется блок else.

alien_color = 'red'
if alien_color == 'green':
    print('You have earned 5 scores!')
else:
    print('You have earned 10 scores!')

#5-5. Цвета 3: преобразуйте цепочку if-else из упражнения 5-4 в цепочку if-elif-else.
#Если переменная содержит значение 'green’, выведите сообщение о том, что игрок только что заработал 5 очков.
#Если переменная содержит значение 'yellow’, выведите сообщение о том, что игрок только что заработал 10 очков.
#Если переменная содержит значение 'red’, выведите сообщение о том, что игрок только что заработал 15 очков.
#Напишите три версии программы и проследите за тем, чтобы для каждого цвета пришельца выводилось соответствующее сообщение.

alien_color = 'red'
if alien_color == 'green':
    print('You have earned 5 scores!')
elif alien_color == 'yellow':
    print('You have earned 10 scores!')
else:
    print('You have earned 15 scores!')

#5-6. Периоды жизни: напишите цепочку if-elif-else для определения периода жизни человека. Присвойте значение переменной age, а затем выведите сообщение.
#Если значение меньше 2 — младенец.
#Если значение больше или равно 2, но меньше 4 — малыш.
#Если значение больше или равно 4, но меньше 13 — ребенок.
#Если значение больше или равно 13, но меньше 20 — подросток.
#Если значение больше или равно 20, но меньше 65 — взрослый.
#Если значение больше или равно 65 — пожилой человек.

print('*'*50)

age = 37

print(f'Ваш возраст {age} лет')
print('Вы:')

if age < 2:
    print('\tМладенец')
elif age < 4:
    print('\tМалыш')
elif age < 13:
    print('\tРебенок')
elif age < 20:
    print('\tПодросток')
elif age < 65:
    print('\tВзрослый')
else:
    print('\tПожилой')

#5-7. Любимый фрукт: составьте список своих любимых фруктов. Напишите серию независимых команд if для проверки того, присутствуют ли некоторые фрукты в списке.
#Создайте список трех своих любимых фруктов и назовите его favorite_fruits.
#Напишите пять команд if. Каждая команда должна проверять, входит ли определенный тип фрукта в список. Если фрукт входит в список,
# блок if должен выводить сообщение вида «You really like bananas!».

my_favourite_fruits = ['apple', 'banana', 'water mellon', 'orange', 'apricot']

print('*'*50)

print('Checking your favourite fruits...')

if 'apple' in my_favourite_fruits:
    print(f'You really like apples!')
if 'banana' in my_favourite_fruits:
    print(f'You really like bananas!')
if 'orange' in my_favourite_fruits:
    print(f'You really like oranges!')
if 'water melon' in my_favourite_fruits:
    print(f'You really like water melons!')
if 'apricot' in my_favourite_fruits:
    print(f'You really like apricots!')

#5-8. Hello Admin: создайте список из пяти и более имен пользователей, включающий имя ‘admin’. Представьте, что вы пишете
# код, который выводит приветственное сообщение для каждого пользователя после его входа на сайт. Переберите элементы списка
# и выведите сообщение для каждого пользователя.
#Для пользователя с именем 'admin’ выведите особое сообщение — например: «Hello admin, would you like to see a status report?»
#В остальных случаях выводите универсальное приветствие — например: «Hello Eric, thank you for logging in again».

print('*'*50)

users = ['OLeg', 'Admin', 'MIke', 'alex', 'viC', 'carAline', 'Andry']

for user in users:
    if user.lower() == 'admin':
        print(f'Hello {user.title()}, would you like to see a status report?')
    else:
        print(f'Hello {user.title()}, thank you for logging in again.')

#5-9. Без пользователей: добавьте в hello_admin.py команду if, которая проверит, что список пользователей не пуст.
#Если список пуст, выведите сообщение: «We need to find some users!»
#Удалите из списка все имена пользователей и убедитесь в том, что программа выводит правильное сообщение.

print('*'*50)

users = []

if users:
    for user in users:
        if user.lower() == 'admin':
            print(f'Hello {user.title()}, would you like to see a status report?')
        else:
            print(f'Hello {user.title()}, thank you for logging in again.')
else:
    print('We need to find some users!')

#5-10. Проверка имен пользователей: выполните следующие действия для создания программы, моделирующей проверку уникальности имен пользователей.
#Создайте список current_users, содержащий пять и более имен пользователей.
#Создайте другой список new_users, содержащий пять и более имен пользователей. Убедитесь в том, что одно или два новых имени
# также присутствуют в списке current_users.
#Переберите список new_users и для каждого имени в этом списке проверьте, было ли оно использовано ранее. Если имя уже
# использовалось, выведите сообщение о том, что пользователь должен выбрать новое имя. Если имя не использовалось,
# выведите сообщение о его доступности.
#Проследите за тем, чтобы сравнение выполнялось без учета регистра символов. Если имя 'John’ уже используется, в регистрации
# имени ‘JOHN’ следует отказать.

print('*'*50)

current_users = ['oleg', 'MAX', 'ALEX', 'boch_54524', 'moNSter112', 'cris']
new_users = ['oleG', 'max', 'cranberries', 'flower323', 'el', 'koshak']

for i in range(len(current_users[:])):
    current_users[i] = current_users[i].lower()

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'The name {new_user} is already in use, please, choose another name.')
    else:
        print(f'The name {new_user} is available!')

#5-11. Порядковые числительные: порядковые числительные в английском языке заканчиваются суффиксом th (кроме 1st, 2nd и 3rd).
#Сохраните числа от 1 до 9 в списке.
#Переберите элементы списка.
#Используйте цепочку if-elif-else в цикле для вывода правильного окончания числительного для каждого числа. Программа должна
# выводить числительные «1st 2nd 3rd 4th 5th 6th 7th 8th 9th», причем каждый результат должен располагаться в отдельной строке.

print('*'*50)

numbers = [i for i in range(1, 10)]
print(numbers)
for number in numbers:
    if number == 1:
        print(f'{number}st', end='')
    elif number == 2:
        print(f' {number}nd', end='')
    elif number == 3:
        print(f' {number}rd', end='')
    else:
        print(f' {number}th')

print('*'*50)

#6-1. Человек: используйте словарь для сохранения информации об известном вам человеке. Сохраните имя, фамилию, возраст и
# город, в котором живет этот человек. Словарь должен содержать ключи с такими именами, как first_name, last_name, age и city.
# Выведите каждый фрагмент информации, хранящийся в словаре.

human = {'name': 'Oleg', 'surname': 'Razumov', 'age': '37', 'city': 'Moscow'}

#6-2. Любимые числа: используйте словарь для хранения любимых чисел. Возьмите пять имен и используйте их как ключи словаря.
# Придумайте любимое число для каждого человека и сохраните его как значение в словаре. Выведите имя каждого человека и его
# любимое число. Чтобы задача стала более интересной, опросите нескольких друзей и соберите реальные данные для своей программы.

favourite_numbers = {'Oleg': 7, 'Andry': 4, 'Nastya': 5}

#6-3. Глоссарий: словари Python могут использоваться для моделирования «настоящего» словаря (чтобы не создавать путаницы,
# назовем его «глоссарием»).
#Вспомните пять терминов из области программирования, которые вы узнали в предыдущих главах. Используйте эти слова как ключи
# глоссария, а их определения — как значения.
#Выведите каждое слово и его определение в аккуратно отформатированном виде. Например, вы можете вывести слово, затем двоеточие
# и определение; или же слово в одной строке, а его определение — с отступом в следующей строке. Используйте символ новой строки
# (\n) для вставки пустых строк между парами «слово-определение» в выходных данных.

programming_terms = {"list": "список упорядоченных значений",
                     "cycle": "цикл, повторяющаяся часть программы",
                     "if-elif-else": "ветвление, исполнение той или иной части когда в зависимости от выполнения условий",
                     "dictionary": "словарь: хэш функция: ключ-значение"}

print('Словарь терминов программирования:')

print(f"List это: {programming_terms['list']}")
print(f"Cycle это: {programming_terms['list']}")
print(f"if-elif-else это: {programming_terms['list']}")
print(f"dictionary это: {programming_terms['list']}")

#6-4. Глоссарий 2: теперь, когда вы знаете, как перебрать элементы словаря, упростите код из упражнения 6-3, заменив серию
# команд print циклом, перебирающим ключи и значения словаря. Когда вы будете уверены в том, что цикл работает, добавьте
# в глоссарий еще пять терминов Python. При повторном запуске программы новые слова и значения должны быть автоматически
# включены в вывод.

print('*'*50)

for name, value in programming_terms.items():
    print(f'{name.title()} это {value}')

#6-5. Реки: создайте словарь с тремя большими реками и странами, по которым протекает каждая река. Одна из возможных пар
# «ключ—значение» — ‘nile’: ‘egypt’.
#Используйте цикл для вывода сообщения с упоминанием реки и страны — например, «The Nile runs through Egypt.»
#Используйте цикл для вывода названия каждой реки, включенной в словарь.
#Используйте цикл для вывода названия каждой страны, включенной в словарь.

print('*'*50)

rivers = {"nile": "egypt", "lena": "russia", "amazonca": "brazil"}

for river, land in rivers.items():
    print(f'The {river.title()} runs trough {land.title()}.')

print('The rivers are: ', end='')
for river in rivers.keys():
    print(f'{river.title()} ', end='')

print('\nThe lands are: ', end='')
for river in rivers.values():
    print(f'{river.title()} ', end='')

#6-6. Опрос: Возьмите за основу код favorite_languages.py (с. 106).
#Создайте список людей, которые должны участвовать в опросе по поводу любимого языка программирования. Включите некоторые
# имена, которые уже присутствуют в списке, и некоторые имена, которых в списке еще нет.
#Переберите список людей, которые должны участвовать в опросе. Если они уже прошли опрос, выведите сообщение с благодарностью
# за участие. Если они еще не проходили опрос, выведите сообщение с предложением принять участие.

print('\n')
print('*'*50)

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people = ['jen', 'oleg', 'max', 'edward']

for person in people:
    if person in favorite_languages.keys():
        print(f'Thank you for taking part in our query, {person.title()}!')
    else:
        print(f'Would you like to take part in our query, {person.title()}?')

print('*'*50)

#6-7. Люди: начните с программы, написанной для упражнения 6-1 (с. 107). Создайте два новых словаря, представляющих разных
# людей, и сохраните все три словаря в списке с именем people. Переберите элементы списка людей. В процессе перебора выведите
# всю имеющуюся информацию о каждом человеке.

human1 = {'name': 'Oleg', 'surname': 'Razumov', 'age': '37', 'city': 'Moscow'}
human2 = {'name': 'Nastya', 'surname': 'Razumova', 'age': '38', 'city': 'Tver'}
human3 = {'name': 'Andry', 'surname': 'Razumov', 'age': '4', 'city': 'Moscow'}

list_of_humans = [human1, human2, human3]

for human in list_of_humans:
    for key, value in human.items():
        print(f'{key} : {value}')
    print('-'*15)

#6-8. Домашние животные: создайте несколько словарей, имена которых представляют клички домашних животных. В каждом словаре
# сохраните информацию о виде животного и имени владельца. Сохраните словари в списке с именем pets. Переберите элементы списка.
# В процессе перебора выведите всю имеющуюся информацию о каждом животном.

Ricchie = {'animal': 'dog', 'name': 'Sergey'}
Sharik = {'animal': 'dog', 'name': 'Max'}
Pushok = {'animal': 'cat', 'name': 'Cataline'}

pets = [Ricchie, Sharik, Pushok]

for pet in pets:
    print(f"animal: {pet['animal']}. owner's name: {pet['name']}")

#6-9. Любимые места: создайте словарь с именем favorite_places. Придумайте названия трех мест, которые станут ключами словаря,
# и сохраните для каждого человека от одного до трех любимых мест. Чтобы задача стала более интересной, опросите нескольких
# друзей и соберите реальные данные для своей программы. Переберите данные в словаре, выведите имя каждого человека и его любимые места.

print('*'*50)

favorite_places = {'Moscow': ['Oleg', 'Andry'],
                   'Turkey': ['Nastya', 'Oleg'],
                   'Romania': ['Andry'],
                   }

for place, persons in favorite_places.items():
    print(f'Place {place} is a favourite place for:')
    for person in persons:
        print(f'\t{person}')

#6-10. Любимые числа: измените программу из упражнения 6-2 (с. 107), чтобы для каждого человека можно было хранить более
# одного любимого числа. Выведите имя каждого человека в списке и его любимые числа.

print('*'*50)

favourite_numbers = {'Oleg': [7, 5, 1], 'Andry': [4, 5, 10], 'Nastya': [5, 1, 15]}

#6-11. Города: создайте словарь с именем cities. Используйте названия трех городов в качестве ключей словаря. Создайте словарь
# с информацией о каждом городе; включите в него страну, в которой расположен город, примерную численность населения и один
# примечательный факт, относящийся к этому городу. Ключи словаря каждого города должны называться country, population и fact.
# Выведите название каждого города и всю сохраненную информацию о нем.

cities = {'Moscow':     {
                            'country': 'Russia',
                            'population': 15000000,
                            'fact': 'capital of Russia'
                        },
            'Tver':     {
                            'country': 'Russia',
                            'population': 500000,
                            'fact': 'City on Volga'
            },
    'Saint-petersburg': {
                            'country': 'Russia',
                            'population': 8000000,
                             'fact': 'Cultural capital'
                        }
         }

for city_name, information in cities.items():
    print(f"Information about the city: {city_name.title()}: \ncountry: {information['country']}, pop. {information['population']}, fact: {information['fact']}")

#6-12. Расширение: примеры, с которыми мы работаем, стали достаточно сложными, и в них можно вносить разного рода усовершенствования.
# Воспользуйтесь одним из примеров этой главы и расширьте его: добавьте новые ключи и значения, измените контекст программы или
# улучшите форматирование вывода.

print('*'*50)

Ricchie = {'nickname': 'Ricchie', 'animal': 'dog', 'name': 'Sergey'}
Sharik = {'nickname': 'Sharik', 'animal': 'dog', 'name': 'Max'}
Pushok = {'nickname': 'Pushok', 'animal': 'cat', 'name': 'Cataline'}

pets = [Ricchie, Sharik, Pushok]

for pet in pets:
    print(f"nickname: {pet['nickname']}. animal: {pet['animal']}. owner's name: {pet['name']}")

#7-1. Прокат машин: напишите программу, которая спрашивает у пользователя, какую машину он хотел бы взять напрокат.
# Выведите сообщение с введенными данными (например, “Let me see if I can find you a Subaru”).

print('*'*50)

car = input('Which car would you like to rent? ')
print('Let me see if I can find you a ' + car)

#7-2. Заказ стола: напишите программу, которая спрашивает у пользователя, на сколько мест он хочет забронировать стол в
# ресторане. Если введенное число больше 8, выведите сообщение о том, что пользователю придется подождать. В противном
# случае сообщите, что стол готов.

print('*'*50)

table = int(input('For how many persons would you like to book a table? '))
if table > 8:
    print('Sorry, but you will have to wait.')
else:
    print('Come in, your table is ready!')

#7-3. Числа, кратные 10: запросите у пользователя число и сообщите, кратно оно 10 или нет.

print('*'*50)

print('This programm is checking if the number is devided into 10:')
number = int(input('Please, enter any number: '))
if number % 10 == 0:
    print('Your number can be devided to 10 fully')
else:
    print('Your number can"t be devided to 10 fully')

#7-4. Дополнения для пиццы: напишите цикл, который предлагает пользователю вводить дополнения для пиццы до тех пор, пока
# не будет введено значение 'quit’. При вводе каждого дополнения выведите сообщение о том, что это дополнение включено в заказ.

flag = True
toppings = []

while flag:

    topping = input('Please, enter pizza topping here: ')

    if topping == 'quit':
        flag = False
        print('You have ordered plain pizza with following topping:\n', toppings)
    else:
        toppings.append(topping)
        print('Thank you for order, any other toppings to your pizza?')

#7-5. Билеты в кино: кинотеатр установил несколько вариантов цены на билеты в зависимости от возраста посетителя. Для
# посетителей младше 3 лет билет бесплатный; в возрасте от 3 до 12 билет стоит $10; наконец, если возраст посетителя
# больше 12, билет стоит $15. Напишите цикл, который предлагает пользователю ввести возраст и выводит цену билета.

print('*'*50)

print('This programm will tell you the ticket price.')

while True:
    print('Please, enter your age below. \n If you would like to stop, type "quit"')
    age = input('--> ')
    if age == 'quit' or age.isalpha():
        break
    age = int(age)
    if age < 3:
        print('The ticket is free!')
    elif age <= 12:
        print('The ticket is 10$')
    else:
        print('The ticket is 15$')

#7-6. Три выхода: напишите альтернативную версию упражнения 7-4 или упражнения 7-5, в которой каждый пункт следующего
# списка встречается хотя бы один раз.
#Завершение цикла по проверке условия в команде while.
#Управление продолжительностью выполнения цикла в зависимости от переменной active.
#Выход из цикла по команде break, если пользователь вводит значение ‘quit’.

flag = True
toppings = []
topping = ''

while topping != 'quit':

    topping = input('Please, enter pizza topping here: ')

    if topping == 'quit':
        print('You have ordered plain pizza with following topping:\n', toppings)
    else:
        toppings.append(topping)
        print('Thank you for order, any other toppings to your pizza?')

#7-7. Бесконечный цикл: напишите цикл, который никогда не завершается, и выполните его. (Чтобы выйти из цикла, нажмите
# Ctrl+C или закройте окно с выводом.)

#message = 'A!'
#while 2 > 1:
#    message = message + 'A!'
#    print(f'{message}')

#7-8. Сэндвичи: создайте список с именем sandwich_orders, заполните его названиями различных видов сэндвичей. Создайте
# пустой список с именем finished_sandwiches. В цикле переберите элементы первого списка и выведите сообщение для каждого
# элемента (например, «I made your tuna sandwich»). После этого каждый сэндвич из первого списка перемещается в список
# finished_sandwiches. После того как все элементы первого списка будут обработаны, выведите сообщение с перечислением
# всех изготовленных сэндвичей.

sandwich_orders = ['tuna sandwich', 'beef sandwich', 'meat sandwich', 'shrimps sandwich',
                   'vegan nut sandwich']
finished_sandwiches = []

while sandwich_orders:
    preparing_sandwich = sandwich_orders.pop()
    print(f'I made your {preparing_sandwich}.')
    finished_sandwiches.append(preparing_sandwich)

print('Following sandwiches has been made: ')

for sandwich in finished_sandwiches:
    print(sandwich)

#7-9. Без пастрами: используя список sandwich_orders из упражнения 7-8, проследите за тем, чтобы значение ‘pastrami’
# встречалось в списке как минимум три раза. Добавьте в начало программы код для вывода сообщения о том, что пастрами
# больше нет, и напишите цикл while для удаления всех вхождений ‘pastrami’ из sandwich_orders. Убедитесь в том, что в
# finished_sandwiches значение ‘pastrami’ не встречается ни одного раза.

sandwich_orders = ['tuna sandwich', 'beef sandwich', 'meat sandwich', 'shrimps sandwich',
                   'vegan nut sandwich', 'pastrami sandwich', 'pastrami sandwich']

print('No more pastrami, sorry!')

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

for sandwich in sandwich_orders:
    print(sandwich)

#7-10. Отпуск мечты: напишите программу, которая опрашивает пользователей, где бы они хотели провести отпуск. Включите
# блок кода для вывода результатов опроса.

vacation_of_dream = {}
flag = True

while flag:
    name = input('Please, enter your name: ')
    land = input('Where would you like to spend your facation? \nPlease, enter here: ')

    vacation_of_dream[name] = land
    stop = input('Would you like to let another person to answer? yes/no ')
    if stop == 'no':
        flag = False
    else:
        continue

print('Answers were following:')

for name, land in vacation_of_dream.items():
    print(f'{name.title()} would like to go to {land.title()} for vacation.')

#8-1. Сообщение: напишите функцию display_message() для вывода сообщения по теме, рассматриваемой в этой главе. Вызовите
# функцию и убедитесь в том, что сообщение выводится правильно.

def display_message():
    '''this function prints a simple message on the screen'''
    print("Currently we're studying functions topic in Python course")

display_message()

#8-2. Любимая книга: напишите функцию favorite_book(), которая получает один параметр title. Функция должна выводить
# сообщение вида «One of my favorite books is Alice in Wonderland». Вызовите функцию и убедитесь в том, что название
# книги правильно передается как аргумент при вызове функции.

def favorite_book(title:str):
    '''
    This function prints information about my favourite book.
    :param title: str
    '''

    print(f'One of my favorite books is {title.title()}.')

favorite_book('Lord of the rings')

#8-3. Футболка: напишите функцию make_shirt(), которая получает размер футболки и текст, который должен быть напечатан на ней.
# Функция должна выводить сообщение с размером и текстом. Вызовите функцию с использованием позиционных аргументов. Вызовите
# функцию во второй раз с использованием именованных аргументов.

def make_shirt(size: str, text:str):
    '''
    This function prints T-shirt information
    :param size: str
    :param text: str
    '''

    print(f'Your T-Shirt is ready.\nSize is: {size}. Text on the T-Shirt is: {text}.')

make_shirt('L', 'Cool Python programmer')
make_shirt(size='L', text='Cool Python programmer')

#8-4. Большие футболки: измените функцию make_shirt(), чтобы футболки по умолчанию имели размер L, и на них выводился текст
# «I love Python.». Создайте футболку с размером L и текстом по умолчанию, а также футболку любого размера с другим текстом.

def make_shirt(size:str='L', text:str='I love Python'):
    '''
    This function prints T-shirt information
    :param size: str
    :param text: str
    '''

    print(f'Your T-Shirt is ready.\nSize is: {size}. Text on the T-Shirt is: {text}.')

make_shirt('L')
make_shirt(size='L', text='Cool Python programmer')

#8-5. Города: напишите функцию describe_city(), которая получает названия города и страны. Функция должна выводить простое
# сообщение (например, «Reykjavik is in Iceland»). Задайте параметру страны значение по умолчанию. Вызовите свою функцию
# для трех разных городов, по крайней мере один из которых не находится в стране по умолчанию.

def describe_city(city:str, land:str='Russia'):
    '''
    Function prints simple message about city and land (input).
    :param city: str
    :param land: str
    '''

    print(f'{city.title()} is in {land.title()}')

describe_city('moscow')
describe_city('tver')
describe_city(city='New-York', land='USA')


#8-6. Названия городов: напишите функцию city_country(), которая получает название города и страну. Функция должна возвращать
# строку в формате “Santiago, Chile”. Вызовите свою функцию по крайней мере для трех пар «город—страна» и выведите возвращенное значение.

def city_country(city: str, country: str) -> str:
    '''
    This simple function return formatted string with city and country names.
    :param city: str
    :param country: str
    :return: str
    '''

    return f'{city.title()}, {country.title()}'

print(city_country('Moscow', 'Russia'))
print(city_country('Tver', 'Russia'))
print(city_country('Santiago', 'Chile'))

#8-7. Альбом: напишите функцию make_album(), которая строит словарь с описанием музыкального альбома. Функция должна
# получать имя исполнителя и название альбома и возвращать словарь, содержащий эти два вида информации. Используйте
# функцию для создания трех словарей, представляющих разные альбомы. Выведите все возвращаемые значения, чтобы показать,
# что информация правильно сохраняется во всех трех словарях.
#Добавьте в make_album() дополнительный параметр для сохранения количества дорожек в альбоме. Если в строку вызова включено
# значение количества дорожек, добавьте это значение в словарь альбома. Создайте как минимум один новый вызов функции с
# передачей количества дорожек в альбоме.

def make_album(singer: str, name: str, tracks_number: int = 0) -> dict:
    '''
    This function return dict with music album description.
    :param singer: str
    :param name: str
    :param tracks_number: int
    :return: dict
    '''
    if tracks_number:
        return {'singer': singer, 'name': name, 'tracks_number': tracks_number}
    else:
        return {'singer': singer, 'name': name}

print(make_album('DDT', 'What is autumn?'))
print(make_album('Deep Purple', 'Smoke on the water'))
print(make_album('DDT', 'What is autumn?', 10))

#8-8. Пользовательские альбомы: начните с программы из упражнения 8-7. Напишите цикл while, в котором пользователь вводит
# исполнителя и название альбома. Затем в цикле вызывается функция make_album() для введенных пользователей и выводится
# созданный словарь. Не забудьте предусмотреть признак завершения в цикле while.

def make_album(singer: str, name: str, tracks_number: int = 0) -> dict:
    '''
    This function return dict with music album description.
    :param singer: str
    :param name: str
    :param tracks_number: int
    :return: dict
    '''
    if tracks_number:
        return {'singer': singer, 'name': name, 'tracks_number': tracks_number}
    else:
        return {'singer': singer, 'name': name}

while True:
    print('Please, enter album information.')
    print('If you would like to escape, type q')
    singer = input('Enter singer name: ')
    if singer == 'q':
        break
    name = input('Enter album name: ')
    if name == 'q':
        break
    tracks_number = input('Enter tracks number: ')
    if tracks_number == 'q':
        break
    print(make_album(singer, name, tracks_number))

#8-9. Фокусники: создайте список с именами фокусников. Передайте список функции show_magicians(), которая выводит имя
# каждого фокусника в списке.

magicians = ['Alfredo', 'Skumbrino', 'Cristian']

def show_magicians(magicians: list):
    '''
    This function prints list on the screen.
    :param magicians: list
    '''

    for magician in magicians:
        print(magician)

show_magicians(magicians)

#8-10. Великие фокусники: начните с копии вашей программы из упражнения 8-9. Напишите функцию make_great(), которая изменяет
# список фокусников, добавляя к имени каждого фокусника приставку «Great». Вызовите функцию show_magicians() и убедитесь в
# том, что список был успешно изменен.

magicians = ['Alfredo', 'Skumbrino', 'Cristian']

def show_magicians(magicians: list):
    '''
    This function prints list on the screen.
    :param magicians: list
    '''

    for magician in magicians:
        print(magician)

def make_great(magicians: list):
    '''
    This function adds "Great " string before the list elements.
    :param magicians: list
    '''

    copy_magicians = magicians[:]
    magicians.clear()

    for magician in copy_magicians:
        magician = 'Great ' + magician
        magicians.append(magician)

make_great(magicians)
show_magicians(magicians)

#8-11. Фокусники без изменений: начните с программы из упражнения 8-10. Вызовите функцию make_great() и передайте ей копию с
# писка имен фокусников. Поскольку исходный список остался неизменным, верните новый список и сохраните его в отдельном
# списке. Вызовите функцию show_magicians() с каждым списком, чтобы показать, что в одном списке остались исходные имена,
# а в другом к имени каждого фокусника добавилась приставка «Great».

magicians = ['Alfredo', 'Skumbrino', 'Cristian']

def show_magicians(magicians: list):
    '''
    This function prints list on the screen.
    :param magicians: list
    '''

    for magician in magicians:
        print(magician)

def make_great(magicians: list) -> list:
    '''
    This function adds "Great " string before the list elements.
    :param magicians: list
    :return magicians: list
    '''

    copy_magicians = magicians[:]
    magicians.clear()

    for magician in copy_magicians:
        magician = 'Great ' + magician
        magicians.append(magician)
    return magicians

great_magicians = make_great(magicians[:])

show_magicians(magicians)
show_magicians(great_magicians)

#8-12. Сэндвичи: напишите функцию, которая получает список компонентов сэндвича. Функция должна иметь один параметр для
# любого количества значений, переданных при вызове функции, и выводить описание заказанного сэндвича. Вызовите функцию
# три раза с разными количествами аргументов.

def sandwiches(*toppings):
    print('The sandwich has following topping:')
    for i in toppings:
        print('- ' + i)

sandwiches('meat', 'vegan', 'fish')

#8-13. Профиль: начните с копии программы user_profile.py. Создайте собственный профиль вызовом build_profile(), укажите
# имя, фамилию и три другие пары «ключ—значение» для вашего описания.

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Oleg', 'Razumov', location='Moscow', field='Telecom')
print(user_profile)

#8-14. Автомобили: напишите функцию для сохранения информации об автомобиле в словаре. Функция всегда должна возвращать
# производителя и название модели, но при этом она может получать произвольное количество именованных аргументов. Вызовите
# функцию с передачей обязательной информации и еще двух пар «имя—значение» (например, цвет и комплектация). Ваша функция
# должна работать для вызовов следующего вида:
#car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)
#Выведите возвращаемый словарь и убедитесь в том, что вся информация была сохранена правильно.

def car_description(vendor: str, model: str, **kwargs) -> dict:
    '''
    This function returns dict with car description
    :param kwargs: any number of params
    :return: dictionary
    '''

    car_desc = {}
    car_desc['vendor'] = vendor
    car_desc['model'] = model

    for key, value in kwargs.items():
        car_desc[key] = value

    return car_desc

print(car_description('VAZ', 'VOLGA', color = 'blue', tow_package = 'True'))

#8-15. Печать моделей: выделите функции примера print_models.py в отдельный файл с именем printing_functions.py. Разместите
# команду import в начале файла print_models.py и измените файл так, чтобы в нем использовались импортированные функции.

import printing_functions

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)

#8-16. Импортирование: возьмите за основу одну из написанных вами программ с одной функцией. Сохраните эту функцию в отдельном
# файле. Импортируйте функцию в файл основной программы и вызовите функцию каждым из следующих способов:

#import имя_модуля

import car_description

print(car_description.car_description('VAZ', 'VOLGA', color = 'blue', tow_package = 'True'))

#from имя_модуля import имя_функции

from car_description import car_description

print(car_description('VAZ', 'VOLGA', color = 'blue', tow_package = 'True'))

#from имя_модуля import имя_функции as псевдоним

from car_description import car_description as cd

print(cd('VAZ', 'VOLGA', color='blue', tow_package='True'))

#import имя_модуля as псевдоним

import car_description as cd

print(cd.car_description('VAZ', 'VOLGA', color='blue', tow_package='True'))

#from имя_модуля import *

from car_description import *

print(car_description('VAZ', 'VOLGA', color='blue', tow_package='True'))

#8-17. Стилевое оформление функций: выберите любые три программы, написанные для этой главы. Убедитесь в том, что в них
# соблюдаются рекомендации стилевого оформления, представленные в этом разделе.

#OK!

#9-1. Ресторан: создайте класс с именем Restaurant. Метод __init__() класса Restaurant должен содержать два атрибута:
# restaurant_name и cuisine_type. Создайте метод describe_restaurant(), который выводит два атрибута, и метод open_restaurant(),
# который выводит сообщение о том, что ресторан открыт.
#Создайте на основе своего класса экземпляр с именем restaurant. Выведите два атрибута по отдельности, затем вызовите оба метода.

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Restaurant has following description:')
        print(f'Restaurant name: {self.restaurant_name}')
        print(f'Restaurant cuisine: {self.cuisine_type}')

    def open_restaurant(self):
        print('Welcome, restaurant is open!')

my_restaurant = Restaurant('Razumoff"s place', 'Middeterian cuisine')

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.restaurant_name

#9-2. Три ресторана: начните с класса из упражнения 9-1. Создайте три разных экземпляра, вызовите для каждого экземпляра метод
# describe_restaurant().

spanish_restaurant = Restaurant('Camida sabrosa', 'Spanish cuisine')
mouse_restaurant = Restaurant('Preipaishon', 'Mouse food')

spanish_restaurant.describe_restaurant()
mouse_restaurant.describe_restaurant()

#9-3. Пользователи: создайте класс с именем User. Создайте два атрибута first_name и last_name, а затем еще несколько атрибутов,
# которые обычно хранятся в профиле пользователя. Напишите метод describe_user(), который выводит сводку с информацией о
# пользователе. Создайте еще один метод greet_user() для вывода персонального приветствия для пользователя.
#Создайте несколько экземпляров, представляющих разных пользователей. Вызовите оба метода для каждого пользователя.

class User():

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def describe_user(self):
        print(f'User information: name: {self.first_name} surname: {self.last_name} email: {self.email} age: {self.age}')

    def greet_user(self):
        print('Hello, ' + self.first_name.title() + ' ' + self.last_name.title() + '!')

Andryusha = User('Andryusha', 'Razumov', 'andry@mail.ru', 4)

Andryusha.describe_user()
Andryusha.greet_user()

papa = User('Oleg', 'Razumov', 'orazumov1983@mail.ru', 37)
papa.greet_user()
papa.describe_user()

mama = User('Nastya', 'Razumova', 'arazumova@mail.ru', 37)
mama.greet_user()
mama.describe_user()


#9-4. Посетители: начните с программы из упражнения 9-1 (с. 165). Добавьте атрибут number_served со значением по умолчанию 0;
# он представляет количество обслуженных посетителей. Создайте экземпляр с именем restaurant. Выведите значение number_served,
# потом измените и выведите снова.
#Добавьте метод с именем set_number_served(), позволяющий задать количество обслуженных посетителей. Вызовите метод с новым
# числом, снова выведите значение.
#Добавьте метод с именем increment_number_served(), который увеличивает количество обслуженных посетителей на заданную величину.
# Вызовите этот метод с любым числом, которое могло бы представлять количество обслуженных клиентов — скажем, за один день.

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Restaurant has following description:')
        print(f'Restaurant name: {self.restaurant_name}')
        print(f'Restaurant cuisine: {self.cuisine_type}')

    def open_restaurant(self):
        print('Welcome, restaurant is open!')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number):
        self.number_served += increment_number

my_restaurant = Restaurant('Razumoff"s place', 'Middeterian cuisine')

print(my_restaurant.number_served)
my_restaurant.number_served = 10
print(my_restaurant.number_served)

my_restaurant.set_number_served(50)
print(my_restaurant.number_served)

my_restaurant.increment_number_served(100)
print(my_restaurant.number_served)


#9-5. Попытки входа: добавьте атрибут login_attempts в класс User из упражнения 9-3 (с. 165). Напишите метод
# increment_login_attempts(), увеличивающий значение login_attempts на 1. Напишите другой метод с именем reset_login_attempts(),
# обнуляющий значение login_attempts.
#Создайте экземпляр класса User и вызовите increment_login_attempts() несколько раз. Выведите значение login_attempts,
# чтобы убедиться в том, что значение было изменено правильно, а затем вызовите reset_login_attempts(). Снова выведите
# login_attempts и убедитесь в том, что значение обнулилось.

class User():

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f'User information: name: {self.first_name} surname: {self.last_name} email: {self.email} age: {self.age}')

    def greet_user(self):
        print('Hello, ' + self.first_name.title() + ' ' + self.last_name.title() + '!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

andryusha = User('Andryusha', 'Razumov', 'andry@mail.ru', 4)

andryusha.describe_user()
andryusha.greet_user()

print(andryusha.login_attempts)
andryusha.increment_login_attempts()
andryusha.increment_login_attempts()
print(andryusha.login_attempts)
andryusha.reset_login_attempts()
print(andryusha.login_attempts)

#9-6. Киоск с мороженым: киоск с мороженым — особая разновидность ресторана. Напишите класс IceCreamStand, наследующий от
# класса Restaurant из упражнения 9-1 (с. 165) или упражнения 9-4 (с. 169). Подойдет любая версия класса; просто выберите ту,
# которая вам больше нравится. Добавьте атрибут с именем flavors для хранения списка сортов мороженого. Напишите метод,
# который выводит этот список. Создайте экземпляр IceCreamStand и вызовите этот метод.

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print('Ice cream flavors:')
        for flavor in self.flavors:
            print(f'- {flavor}')


my_IceCreamStand = IceCreamStand('Razumoff_ice_cream', 'ice cream', 'vanila', 'chocolate', 'lemon', 'watermelon')

my_IceCreamStand.show_flavors()

#9-7. Администратор: администратор — особая разновидность пользователя. Напишите класс с именем Admin, наследующий от класса
# User из упражнения 9-3 (с. 165) или упражнения 9-5 (с. 170). Добавьте атрибут privileges для хранения списка строк вида
# «разрешено добавлять сообщения», «разрешено удалять пользователей», «разрешено банить пользователей» и т. д. Напишите
# метод show_privileges() для вывода набора привилегий администратора. Создайте экземпляр Admin и вызовите свой метод.

class Admin(User):

    def __init__(self, first_name, last_name, email, age, *privileges):
        super().__init__(first_name, last_name, email, age)
        self.privileges = privileges

    def show_privileges(self):
        print('User privileges:')
        for priv in self.privileges:
            print(f'- {priv}')

my_admin = Admin('Oleg', 'Razumov', 'orazumov1983@mail.ru', 37, 'разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей')

my_admin.show_privileges()
my_admin.describe_user()

#9-8. Привилегии: напишите класс Privileges. Класс должен содержать всего один атрибут privileges со списком строк из
# упражнения 9-7. Переместите метод show_privileges() в этот класс. Создайте экземпляр Privileges как атрибут класса Admin.
# Создайте новый экземпляр Admin и используйте свой метод для вывода списка привилегий.

class User():

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f'User information: name: {self.first_name} surname: {self.last_name} email: {self.email} age: {self.age}')

    def greet_user(self):
        print('Hello, ' + self.first_name.title() + ' ' + self.last_name.title() + '!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

andryusha = User('Andryusha', 'Razumov', 'andry@mail.ru', 4)

andryusha.describe_user()
andryusha.greet_user()

class Privileges():

    def __init__(self, privileges=['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей']):
        self.privileges = privileges

    def show_privileges(self):
        print('User privileges:')
        for priv in self.privileges:
            print(f'- {priv}')


class Admin(User):

    def __init__(self, first_name, last_name, email, age):
        super().__init__(first_name, last_name, email, age)
        self.privileges = Privileges()


my_admin = Admin('Oleg', 'Razumov', 'orazumov1983@mail.ru', 37)

my_admin.privileges.show_privileges()
my_admin.describe_user()

#9-9. Обновление аккумулятора: используйте окончательную версию программы electric_car.py из этого раздела. Добавьте в
# класс Battery метод с именем upgrade_battery(). Этот метод должен проверять размер аккумулятора и устанавливать мощность
# равной 85, если она имеет другое значение. Создайте экземпляр электромобиля с аккумулятором по умолчанию, вызовите
# get_range(), а затем вызовите get_range() во второй раз после вызова upgrade_battery(). Убедитесь в том, что запас
# хода увеличился.

class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):

        print('Checking battery size...')

        if self.battery_size != 85:
            self.battery_size = 85
            print('Your battery is upgraded to 85-kWh!')

        else:
            print('Your battery is currently 85 kWh.')

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

#9-10. Импортирование класса Restaurant: возьмите последнюю версию класса Restaurant и сохраните ее в модуле. Создайте отдельный
# файл, импортирующий класс Restaurant. Создайте экземпляр Restaurant и вызовите один из методов Restaurant, чтобы показать, что
# команда import работает правильно.

import class_restaurant

my_restaurant = class_restaurant.Restaurant('Razumoff"s place', 'Middeterian cuisine')

my_restaurant.increment_number_served(100)
print(my_restaurant.number_served)

print(my_restaurant.describe_restaurant())

#9-11. Импортирование класса Admin: начните с версии класса из упражнения 9-8 (с. 176). Сохраните классы User, Privileges и
# Admin в одном модуле. Создайте отдельный файл, создайте экземпляр Admin и вызовите метод show_privileges(), чтобы показать,
# что все работает правильно.

from user_module import Admin

my_admin = Admin('Oleg', 'Razumov', 'orazumov1983@mail.ru', 37)

my_admin.privileges.show_privileges()
my_admin.describe_user()

#9-12. Множественные модули: сохраните класс User в одном модуле, а классы Privileges и Admin в другом модуле. В отдельном
# файле создайте экземпляр Admin и вызовите метод show_privileges(), чтобы показать, что все работает правильно.

from user import User

class Privileges():
# ####

class Admin(User):
# ####

######

from user import User
from admin_privilegies import Privileges, Admin

my_admin = Admin('Oleg', 'Razumov', 'orazumov1983@mail.ru', 37)

my_admin.privileges.show_privileges()
my_admin.describe_user()

#9-13. Переработка с OrderedDict Rewrite: начните с упражнения 6-4 (с. 113), в котором стандартный словарь используется для
# представления глоссария. Перепишите программу с использованием класса OrderedDict и убедитесь в том, что порядок вывода
# совпадает с порядком добавления пар «ключ—значение» в словарь.

from collections import OrderedDict

programming_terms = OrderedDict()

programming_terms = {
                     "cycle": "цикл, повторяющаяся часть программы",
                     "if-elif-else": "ветвление, исполнение той или иной части когда в зависимости от выполнения условий",
                     "dictionary": "словарь: хэш функция: ключ-значение",
                     "list": "список упорядоченных значений"
                    }

for name, value in programming_terms.items():
    print(f'{name.title()} это {value}')

#9-14. Кубики: модуль random содержит функции для генерирования случайных чисел разными способами. Функция randint() возвращает
# целое число в заданном диапазоне. Следующий код возвращает число от 1 до 6:
#from random import randint
#x = randint(1, 6)
#Создайте класс Die с одним атрибутом с именем sides, который содержит значение по умолчанию 6. Напишите метод roll_die()
# для вывода случайного числа от 1 до количества сторон кубика. Создайте экземпляр, моделирующий 6-гранный кубик, и
# имитируйте 10 бросков.
#Создайте модели 10- и 20-гранного кубика. Имитируйте 10 бросков каждого кубика.

from random import randint

class Die():
    '''
    Класс имитирует выкидываение N-гранного кубика.
    По умолчанию - 6 граней.
    '''

    def __init__(self, sides=6):
        self.sides = sides
        print(f'Die has {self.sides} sides.')

    def roll_die(self):
        x = randint(1, self.sides)
        print(f'Roll die: {x}')

die1 = Die()
for i in range(10):
    die1.roll_die()

die2 = Die(10)
for i in range(10):
    die2.roll_die()

die3 = Die(20)
for i in range(10):
    die3.roll_die()

die1 = Die(100000)
for i in range(1, 11, 1):
    print('Бросок номер', i)
    die1.roll_die()

#9-15. Модуль недели: для знакомства со стандартной библиотекой Python отлично подойдет сайт Python Module of the Week.
# Откройте сайт http://pymotw.com/ и просмотрите оглавление. Найдите модуль, который покажется вам интересным, и прочитайте
# про него или изучите документацию по модулям collections и random.

# OK!

#10-1. Изучение Python: откройте пустой файл в текстовом редакторе и напишите несколько строк текста о возможностях Python.
# Каждая строка должна начинаться с фразы: «In Python you can…» Сохраните файл под именем learning_python.txt в каталоге,
# использованном для примеров этой главы. Напишите программу, которая читает файл и выводит текст три раза: с чтением всего
# файла, с перебором строк объекта файла и с сохранением строк в списке с последующим выводом списка вне блока with.

with open('texts/learning_python.txt') as file:
    content = file.read()
    print(content)

print('*'*50)

with open('texts/learning_python.txt') as file:
    for line in file:
        print(line.strip())

print('*'*50)

with open('texts/learning_python.txt') as file:
    lines = file.readlines()

for i in lines:
    print(i.strip())

#10-2. Изучение C: метод replace() может использоваться для замены любого слова в строке другим словом. В следующем примере
# слово ‘dog’ заменяется словом ‘cat’:
#>>> message = "I really like dogs."
#>>> message.replace('dog', 'cat')
#'I really like cats.'
#Прочитайте каждую строку из только что созданного файла learning_python.txt и замените слово Python названием другого языка,
# например C. Выведите каждую измененную строку на экран.

with open('texts/learning_python.txt') as file:
    for line in file:
        line = line.replace('Python', 'C')
        print(line)

#10-3. Гость: напишите программу, которая запрашивает у пользователя его имя. Введенный ответ сохраняется в файле с именем
# guest.txt.

print('Введите, пожалуйста, своё имя для сохранения в файл:')
name = input('$> ')

with open('texts/guest.txt','a') as file:
    file.write(f'\n{name}')

#10-4. Гостевая книга: напишите цикл while, который в цикле запрашивает у пользователей имена. При вводе каждого имени
# выведите на экран приветствие и добавьте строку с сообщением в файл с именем guest_book.txt. Проследите за тем, чтобы
# каждое сообщение размещалось в отдельной строке файла.

print('Введите, пожалуйста, своё имя для сохранения в файл:')
print('Для выхода нажмите q')

name = ''

with open('texts/guest_book.txt', 'a') as file:
    while True:
        name = input('$> ')
        if name == 'q':
            break
        file.write(f'{name}\n')

#10-5. Опрос: напишите цикл while, в котором программа спрашивает у пользователя, почему ему нравится программировать.
# Каждый раз, когда пользователь вводит очередную причину, сохраните текст его ответа в файле.

print('Введите, пожалуйста, ответ на вопрос "Почему вам нравится программировать?" он сохранится в файл.')
print('Для выхода нажмите q')

answer = ''

with open('texts/query.txt', 'a') as file:
    while True:
        answer = input('$> ')
        if answer == 'q':
            break
        file.write(f'{answer}\n')

#10-6. Сложение: при вводе числовых данных часто встречается типичная проблема: пользователь вводит текст вместо чисел.
# При попытке преобразовать данные в int происходит исключение TypeError. Напишите программу, которая запрашивает два числа,
# складывает их и выводит результат. Перехватите исключение TypeError, если какое-либо из входных значений не является числом,
# и выведите удобное сообщение об ошибке. Протестируйте свою программу: сначала введите два числа, а потом введите текст
# вместо одного из чисел.

print('Программа складывает два числа.')

try:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
except ValueError:
    print('Введите, пожалуйста, число.')
else:
    print(f'Сумма двух чисел: {a + b}')

#10-7. Калькулятор: заключите код из упражнения 10-6 в цикл while, чтобы пользователь мог продолжать вводить числа, даже
# если он допустил ошибку и ввел текст вместо числа.

print('Программа складывает два числа.')
print('Для выхода введите q')

flag = True
while flag == True:
    try:
        a = int(input('Введите первое число: '))
        if a == 'q':
            break
        b = int(input('Введите второе число: '))
        if b == 'q':
            break
    except ValueError:
        print('Введите, пожалуйста, число.')
    else:
        print(f'Сумма двух чисел: {a + b}')

#10-8. Кошки и собаки: создайте два файла с именами cats.txt и dogs.txt. Сохраните минимум три клички кошек в первом файле
# и три клички собак во втором. Напишите программу, которая пытается прочитать эти файлы и выводит их содержимое на экран.
# Заключите свой код в блок try-except для перехвата исключения FileNotFoundError и вывода понятного сообщения об отсутствии
# файла. Переместите один из файлов в другое место файловой системы; убедитесь в том, что код блока except выполняется,
# как и положено.

filenames = ['texts/cats.txt', 'texts/dogs.txt']

def open_file(filename):

    try:
        with open(filename, encoding='UTF-8') as file:
            print(file.name)
            content = file.readlines()
            for i in content:
                print(i.strip())

    except FileNotFoundError:
        print(f'Файл {filename} не был найден по указанному адресу.')

for filename in filenames:
    open_file(filename)

#10-9. Ошибки без уведомления: измените блок except из упражнения 10-8 так, чтобы при отсутствии файла программа продолжала
# работу, не уведомляя пользователя о проблеме.

filenames = ['texts/cats.txt', 'texts/dogs.txt']

def open_file(filename):

    try:
        with open(filename, encoding='UTF-8') as file:
            print(file.name)
            content = file.readlines()
            for i in content:
                print(i.strip())

    except FileNotFoundError:
        pass

for filename in filenames:
    open_file(filename)

#10-10. Частые слова: зайдите на сайт проекта «Гутенберг» (http://gutenberg.org/) и найдите несколько книг для анализа.
# Загрузите текстовые файлы этих произведений или скопируйте текст из браузера в текстовый файл на вашем компьютере.
#Для подсчета количества вхождений слова или выражения в строку можно воспользоваться методом count(). Например, следующий
# код подсчитывает количество вхождений ‘row’ в строке:
#>>> line = "Row, row, row your boat"
#>>> line.count('row')
#2
#>>> line.lower().count('row')
#3
#Обратите внимание: преобразование строки к нижнему регистру функцией lower() позволяет найти все вхождения искомого слова
# независимо от регистра.
#Напишите программу, которая читает файлы из проекта «Гутенберг» и определяет количество вхождений слова ‘the’ в каждом тексте.

filename = 'texts/An Account of the Ladies of Llangollen.txt'

with open(filename, 'r', encoding='UTF-8') as file:
    content = file.read()
    print(content.lower().count('the'))

#10-11. Любимое число: напишите программу, которая запрашивает у пользователя его любимое число. Воспользуйтесь функцией
# json.dump() для сохранения этого числа в файле. Напишите другую программу, которая читает это значение и выводит сообщение:
# «Я знаю ваше любимое число! Это _____».

import json

print('Please, enter your favourite number to save it into file.')

number = int(input('$> '))

filename = 'texts/fav_number.json'

with open(filename, 'w') as file:
    json.dump(number, file)

with open(filename, 'r') as file:
    number_file = json.load(file)

print(f'Your favourite number was saved into file {filename}. The number is {number_file}.')

#10-12. Сохраненное любимое число: объедините две программы из упражнения 10-11 в один файл. Если число уже сохранено,
# сообщите его пользователю, а если нет — запросите любимое число пользователя и сохраните в файле. Выполните программу
# дважды, чтобы убедиться в том, что она работает.

import json

print('Searching for your favourite number...')

filename = 'texts/fav_number.json'

try:
    with open(filename, 'r') as file:
        number_file = json.load(file)
except FileNotFoundError:
    print('Not found. Please, enter your favourite number to save it into file.')
    number = int(input('$> '))

    with open(filename, 'w') as file:
        json.dump(number, file)
    print(f'Your favourite number is saved into file {filename}. The number is {number}.')

else:
    print(f'Your favourite number is saved into file {filename}. The number is {number_file}.')

#10-13. Проверка пользователя: последняя версия remember_me.py предполагает, что пользователь либо уже ввел свое имя,
# либо программа выполняется впервые. Ее нужно изменить на тот случай, если текущий пользователь не является тем человеком,
# который последним использовал программу.
#Прежде чем выводить приветствие в greet_user(), спросите пользователя, правильно ли определено имя пользователя. Если
# ответ будет отрицательным, вызовите get_new_username() для получения правильного имени пользователя.


import json

def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Приветствует пользователя по имени."""

    username = get_stored_username()

    if username:

        answer = input(f'Hello, is your name: {username}? (yes/no) ')

        if answer == 'yes':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()

#11-1. Город, страна: напишите функцию, которая получает два параметра: название страны и название города. Функция должна
# возвращать одну строку в формате «Город, Страна», например «Santiago, Chile». Сохраните функцию в модуле с именем city_functions.py.
#Создайте файл test_cities.py для тестирования только что написанной функции (не забудьте импортировать unittest и тестируемую
# функцию). Напишите метод test_city_country() для проверки того, что вызов функции с такими значениями, как ‘santiago’
# и ‘chile’, дает правильную строку. Запустите test_cities.py и убедитесь в том, что тест test_city_country() проходит успешно.

def city_functions(land, city):

    return f'{city.title()}, {land.title()}'

# ----------------------------------------------------

import unittest
from city_function import city_functions

class CityLandFormat(unittest.TestCase):

    def test_city_land_format_name(self):
        formatted_name = city_functions(land='Chile', city='Santiago')
        self.assertEqual(formatted_name, 'Santiago, Chile')

unittest.main()

#11-2. Население: измените свою функцию так, чтобы у нее был третий обязательный параметр — население. В новой версии
# функция должна возвращать одну строку вида «Santiago, Chile — population 5000000.» Снова запустите программу test_cities.py.
# Убедитесь в том, что тест test_city_country() на этот раз не проходит.
#Измените функцию так, чтобы параметр населения стал необязательным. Снова запустите test_cities.py и убедитесь в том, что
# тест test_city_country() проходит успешно.

def city_functions(land, city, population=''):
    if population == '':
        return f'{city.title()}, {land.title()}'
    else:
        return f'{city.title()}, {land.title()} - population {population}'

#Напишите второй тест test_city_country_population(), который проверяет вызов функции со значениями ‘santiago’, ‘chile’ и
# ‘population=5000000’. Снова запустите test_cities.py и убедитесь в том, что новый тест проходит успешно.

import unittest
from city_function import city_functions

class CityLandFormat(unittest.TestCase):

    def test_city_land_format_name_pop(self):
        formatted_name = city_functions(land='Chile', city='Santiago', population='5000000')
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')

    def test_city_land_format_name(self):
        formatted_name = city_functions(land='Chile', city='Santiago')
        self.assertEqual(formatted_name, 'Santiago, Chile')

unittest.main()

#11-3. Работник: напишите класс Employee, представляющий работника. Метод __init__() должен получать имя, фамилию и ежегодный
# оклад; все эти значения должны сохраняться в атрибутах. Напишите метод give_raise(), который по умолчанию увеличивает
# ежегодный оклад на $5000 — но при этом может получать другую величину прибавки.
#Напишите тестовый сценарий для Employee. Напишите два тестовых метода, test_give_default_raise() и test_give_custom_raise().
# Используйте метод setUp(), чтобы вам не приходилось заново создавать экземпляр Employee в каждом тестовом методе. Запустите
# свой тестовый сценарий и убедитесь в том, что оба теста прошли успешно.

class Employee():

    def __init__(self, name: str, surname: str, year_salary: int):
        self.name = name
        self.surname = surname
        self.year_salary = year_salary

    def give_raise(self, add: int = 5000):
        self.year_salary += add


# -------------------------------------

import unittest
from employee import Employee

class TestRaisesForEmployee(unittest.TestCase):

    def setUp(self) -> None:

        self.my_employee = Employee('Oleg', 'Razumov', 15000)
        self.add = 500

    def test_give_default_raise(self):

        self.my_employee.give_raise()
        self.assertEquals(self.my_employee.year_salary, 20000)

    def test_give_custom_raise(self):

        self.my_employee.give_raise(self.add)
        self.assertEquals(self.my_employee.year_salary, 15500)

unittest.main()

