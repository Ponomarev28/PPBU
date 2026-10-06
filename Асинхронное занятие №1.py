# Цикл for

# Пример с началом и концом

# for i in range(1, 5):
#     print(i, end=' ')
# # Пример с началом, концом и шагом
#
# for i in range(1, 5,2):
#     print(i, end=' ')

# Узор с помощью цикла

# import turtle as t
#
# t.ht()
# t.pensize(3)
# t.color('blue')
# # t.rt(60)
# for i in range(4, 56, 4):
#     t.fd(i)
#     t.rt(90)
# t.lt(90)
# for i in range(52, 0, -4):
#     t.fd(i)
#     t.rt(90)

# Круги

import turtle as t
import time

t.speed(0)
t.ht()
r = 20
t.pensize(4)
t.color('#FFA500')
t.fillcolor('#A200FF')

for k in range(3):
    print('______k =' + str(k))
    for j in range(4):
        print('___j = ' + str(j))
        for i in range(6):
            print('i = ' + str(i))
            t.begin_fill()
            t.circle(r)
            t.end_fill()
            t.rt(60)
            time.sleep(0.1)
        r = r - 5
    t.pu()
    t.fd(80)
    t.pd()
    r = 20

# Диапазон внутри цикла
#
# import turtle as t
#
# t.ht()
# t.pensize(5)
#
# for r in range(40, 0, -10):
#     for i in range(6):
#         t.begin_fill()
#         t.color('#FFA500')
#         t.fillcolor('#A200FF')
#         t.circle(r)
#         t.end_fill()
#         t.rt(60)

# Индексы

# text = "Hello"
# print(range(40, 0, -10)[1])

# Срезы

# text = "Python это круто!"
#
# s = text[-7:-2] # Отрицательный диапазон
#
# print(s)

# text = "Привет как дела"
#
# s = text[:6] # Диапазон первых символов
#
# print(s)

# text = "Это последние символы"
#
# s = text[-5:] # Диапазон последних символов
#
# print(s)

# text = "12345678"
#
# s = text[::2] # Шаг диапазона как в range
#
# print(s)

# text = "Аргенитина манит негра"
#
# s = text[::-1]  # Переворот строки задом наперед
#
# print(s)

# text = "Разделить строку"
#
# x = 10 # Задаем символ до и после которого будем делать срез
#
# p_1 = text[:x] # Извлекаем первую часть
#
# p_2 = text[x:] # Извлекаем вторую часть
#
# print(p_1, p_2, sep='\n')

# text = 'Пример текстовой строки'
#
# s = text[8:15] # Задаем дипазон от и до которого делаем срез
#
# print(s)

# --- Ветвления ---

# n = input("Введите число: " )
#
#
# if n.isdigit() or (n[0] == '-') and n[1:].isdigit():
#     n = int(n)
#     if n < 0:
#         print("число отрицательное")
#     elif n > 0:
#         print("число положительное")
#     else:
#         print("число ноль")
# else:
#     print('вы ввели не число')


# --- Перевод в нижний регистр и преобразование первой буквы в заглавную ---
# s = input('Введите время года: ')
# s = s.lower() # lower() - перевод в нижний регистр
# if s == 'лето':
#     print(f' {s.capitalize()} - прекрасное время для отдыха на пляже') # capitalize() - перевод первой буквы в заглавную
# elif s == 'осень':
#     print('Хорошее время для прогулок в парке')

# --- Логические операторы ---

# s = input('Введите номер сотового телефона без +7: ')
# if len(s) == 10 and s[0] == '9':  # len - длина строки (в символах)
#     print('Это номер сотового телефона')
# else:
#     print('Это не номер сотового телефона')





