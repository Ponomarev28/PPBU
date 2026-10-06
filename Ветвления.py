"""Операции сравнения"""
""" >, <, >=, <=, ==, !="""

"""
(), not, and, or
True and True and True(False) ... = True(False)
False or False(True) ... = False(True)
"""

# a = 56
# b = 56
# c = a > b
# print(c)
#
# z = a > b and a >= b a != b
# z1 = a < b or <= b or a != b


# if a > b:
#     print('A > B')
# elif a < b:
#     print('A < B')
# else:
#     print('A = B')
# print('END')

# h = float(input('Введите время суток:'))
# if h >= 4 and h < 12:
#     print('Morning')
# elif h >= 12 and h < 17:
#     print('Afternoon')


color = input('Цвет светофора:')
match color:
    case 'red' | 'no': print('STOP')
    case 'green': print('GO')
    case 'yellow': print('READY')
    case _: print('UNKNOWN')
