'''Работа со строками'''

# t = 'Это тестовая строка текста'
# p = 'в'
# print(f'Подстрока "{p}" найдена в {t.find(p)} позиции.')

# t = 'Я люблю яблоки, потому что яблоки вкусные!'
# s = t.replace(',', '')
# s2 = s.replace('!', '')
# print(s2)

# s = 'Имена сотрудников отдела: Артём Иванов, Артём Филатов, Егор Нестеров, Артём'
# print(f'В нашем отделе {s.count('Артём')} Артёма')

# t = input('Введите расстояние:')
#
# if t.endswith('см'):
#     print('Это расстояние в сантиметрах')
# elif t.endswith('мм'):
#     print('Это расстояние в миллиметрах')

# s = input('Введите ФИО: ')
# f, i, o = s.split()
# print(f'Фамилия: {f}')
# print(f'Имя: {i}')
# print(f'Отчество: {o}')
#
# str = f'| {f} | {i} | {o} |'
# print('-' * len(str))
# print(str)
# print('-' * len(str))

# s1 = [1, 2, 3, 4 , 5]
# s1.insert(6, 10)
# print(s1)
# s1.append(6)
# print(s1)
# print(s1[0])
# s2 = ['a', 'w', 'y']
# s1.extend(s2)
# s4 = s1 + s2
# print(s4)
# s2.append('s')
# print(s2)
# print(s2[1])
# s3 = [[1, 2, 3], ['q', 'w', 'f']]
# s4 = s3 * 2
# print(s4)
# s3.append([7, 'i', 3])
# print(s3)
# print(s3[1][1])

# k1 = (10, 12, 14, 16)
# k2 = (22, 24)
# k3 = k1 * k2
# k4 = k1 * 2
# print(k4)

# s2 = ['яблоко', 'банан', 'апельсин']
# s3 = s2.reverse()
# print(s2)
# print(s3)
# s1[0] = 2
# s1.remove(3)
# print(s1[:3])
# k = (11, 13, 15, 17, 19)
# print(k[::2])

# s1 = [1, 100, 12, 55, 33, 8, 14]
# s4 = s1.sort()
# print(s1)
# print(s4)
#
# s2 = ['мылом', 'мама', 'мыла', 'машу']
# s2.sort()
# print(s2)

# t = 'вихри снежные крутя'
# s = tuple(t)
#
# print(s.count('ю'))

# k = [-888, -785, -25]
# print(f'Минимальный элемент списка {k} равен {min(k)}')

# url = 'C:\Python\Leson\2020\Lesson05.py'
# f = url.split('\\')
# print(f[-1])

# s = [1, 2, 3, 4, 5]
# k = (10, 20, 30, 40, 50)
# t = ['буря', 'мглою', 'небо', 'кроет',]
# i = 0
# while i < len(s):
#     if s[i] == 3:
#         i += 1
#         continue
#     print(s[i] * 100)
#     i += 1

import random

for i in range(10):
    a1 = str(random.randint(1, 9999))
    a2 = str(random.randint(1, 9999))
    a3 = str(random.randint(1, 9999))
    print(f'| {a1:>4} \t| | {a2:>4} \t| | {a3:>4} \t|')