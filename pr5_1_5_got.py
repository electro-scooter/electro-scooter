print('''# 1. Создайте словарь, в котором ключами будут числа от 1 до 10, 
# а значениями эти же числа, возведенные в куб
''')
my_dict = {}
for elem in range(1, 11):
    my_dict.update({elem: elem ** 3})
print('Результат')
print(my_dict)

print('''
# 2. Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd': 600}.
# Объедините их в один при помощи встроенных функций языка Python.
''')

dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)

print('''
# 3. Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.
# {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
''')
result = 1
my_dict = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
for val in my_dict:
    values = my_dict.values()
# values = list(values)
for val in values:
    result *= val
print(result)

print('''
# 4. Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом, чтобы элементы первого списка
# были ключами, а элементы второго — соответственно значениями нашего словаря.
# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
''')
keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']
my_dict = {}

for i in range(len(keys)):  # готовое решение
    my_dict[keys[i]] = values[i]
print(my_dict)

print('''
# 5. Создайте словарь из строки 'hello world' следующим образом: в качестве ключей возьмите буквы строки,
# а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.
''')

# str1 = 'hello world'
# my_dict = {i: str1.count(i) for i in str1} # готовое решение
# print(my_dict)

# dct = {}
# for i in 'hello world':
#     dct[i] = dct.setdefault(i, 0) + 1  # готовое решение
# print(dct)

my_string = 'hello world'
set_string = {my_string, }
my_dict = {}
counter = 0
# print('SET', set_string)
keys = list(my_string)
# print('KEYS',keys)
for i in keys:
    counter = keys.count(i)
    # print(i,counter)
    my_dict.update({i: counter})
print('DICT', my_dict)

print('''# 6. Доработать игру quiz с вариантами выбора и выбором ИИ. (Выбирается случайный ответ)
''')
# НЕ СДЕЛАНО
# НЕ СДЕЛАНО
# НЕ СДЕЛАНО

# name = input('Введите имя/название команды: ')
# print(f'Отлично! {name.capitalize()}, давайте начнем!')
counter_1 = 0
counter_2 = 0

questions = {
    'Как называется самая известная смотровая площадка Москвы?': 'воробьёвы горы',
    'Известный код из Матрицы на самом деле обозначает ...': 'рецепт суши',
    'Что в море является ориентиром для моряка': 'полярная звезда'
}
variants = [questions.values()]

for question in questions:
    print(question)
    print(variants)
    # answer_1 = input('Выберите ответ 1,2,3?: \t')

    # if answer in questions[question]:
    #     counter += 1

print(f'Ваш счет: {counter}')  # счетчик очков
if counter >= 2:
    print('Вы победили в игре!')
else:
    print('К сожалению вы програли ;c')

print('''
# 7. Доработать игру scrabble с поддержкой англ языка
''')
points_ru = {
    'АВЕИНОРСТ': 1,
    'ДКЛМПУ': 2,
    'БГЁЬЯ': 3,
    'ЙЫ': 4,
    'ЖЗХЦЧ': 5,
    'ШЭЮ': 8,
    'ФЩЪ': 10
}
points_en = {
    'AEIOULNSTR': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10
}
lang = int(input('Выберите язык / Choose language \n 1 - русский \t 2 - english'))
if lang == 1:
    word = input('Введите слово: \n').upper()
    points_counter = 0
    for letter in word:
        for key in points_ru.keys():
            if letter in key:
                points_counter += points_ru[key]
                continue
    print('Вы заработали ', points_counter, ' очков')
elif lang == 2:
    word = input('Input word: \n').upper()
    points_counter = 0
    for letter in word:
        for key in points_en.keys():
            if letter in key:
                points_counter += points_en[key]
                continue
    print('You have ', points_counter, ' points')
else:
    print('Неверный выбор')


# Упражнение 53. Азбука Морзе. Азбука Морзе зашифровывает буквы и цифры при помощи
# точек и тире. В данном упражнении вам необходимо написать программу, в которой
# соответствие символов из азбуки Морзе будет храниться в виде словаря. В табл. 6.3
# приведена та часть азбуки, которая вам понадобится при решении этого задания. В
# основной программе вам необходимо запросить у пользователя строку. После этого
# программа должна преобразовать его в соответствующую последовательность точек
# и тире, вставляя пробелы между отдельными символами. Символы, не представленные
# в таблице, можно игнорировать. Например, сообщение Hello, World! может быть
# представлено следующей последовательностью: .... . .–.. .–.. ––– .–– ––– .–. .–.. –..