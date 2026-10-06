"""Для факультативных занятий"""
from operator import length_hint

# Вторая задача
# name = input()
# city = input()
# role = input()
#
# print('=== КАРТОЧКА УЧАСТНИКА ===', f'Имя: {name}', f'Город: {city}', f'Роль: {role}', f'Добро пожаловать, {name}!', sep='\n')

# Третья задача

# name = input()
# departure = input()
# destination = input()
# flight = input()
# seat = input()
#
# print('================================',
#       'ПОСАДОЧНЫЙ ТАЛОН',
#       f'Пассажир: {name}',
#       f'Маршрут: {departure} -> {destination}',
#       f'Рейс: {flight}',
#       f'Место: {seat}',
#       '================================',
#       sep='\n')

# Четвертая задача

# a_name = input()
# b_name = input()
# c_name = input()
# d_name = input()
#
# print('ПЕРЕСАДКА ЗАВЕРШЕНА',
#       f'Модуль Альфа: {d_name}',
#       f'Модуль Бета: {a_name}',
#       f'Модуль Гамма: {b_name}',
#       f'Модуль Дельта: {c_name}',
#       sep='\n')

# Пятая задача

# comander_name = input()
# ship_name = input()
# planet_name = input()
# goal = input()
# channel = input()
#
# print('=== ПРОТОКОЛ СВЯЗИ ===',
#       f'Канал: {channel}',
#       f'Планета: {planet_name}',
#       f'Корабль: {ship_name}',
#       f'Командир: {comander_name}',
#       f'Цель: {goal}',
#       f'Сообщение: {planet_name}, корабль «{ship_name}» вышел на связь!',
#       sep='\n')

# Шестая задача

# total_power = int(input()) + int(input()) + int(input())
# consumption = int(input())
#
# print(f'Получено: {total_power}',
#       f'Израсходовано: {consumption}',
#       f'Осталось: {total_power - consumption}',
#       sep='\n')

# Седьмая задача

# small_cargo_quantity = int(input())
# small_cargo_weight = int(input())
# big_cargo_quantity = int(input())
# big_cargo_weight = int(input())
# ship_mass = int(input())
#
# print(f'Масса груза: {small_cargo_quantity * small_cargo_weight + big_cargo_quantity * big_cargo_weight}',
#       f'Общая масса: {small_cargo_quantity * small_cargo_weight + big_cargo_quantity * big_cargo_weight + ship_mass}',
#       sep='\n')

# Восьмая задача

# length = int(input())
# width = int(input())
# price = int(input())
#
# square = length * width
# perimeter = 2 * (length + width)
# price_for_square = price * square
#
# print(f'Площадь: {square}',
#       f'Периметр: {perimeter}',
#       f'Стоимость покрытия: {price_for_square}',
#       sep='\n')

# Девятая задача

# length = int(input())
#
# v = length ** 3
# s = length ** 2 * 6
# l = length * 12
#
# print(f'Объём: {v}')
# print(f'Площадь поверхности: {s}')
# print(f'Длина каркаса: {l}')

# Десятая задача

# c = int(input())
#
# f = c * 9 / 5 + 32
#
# print(f'Температура по Фаренгейту: {float(f)}')

# Одинадцатая задача

# t = int(input())
#
# hour = t // 60
# minute = t % 60
#
# print(f'Часы: {hour}',
#       f'Минуты: {minute}',
#       sep='\n')

# Двенадцатая задача

# n = int(input())
#
# d = n // 86400
# n = n % 86400
# h = n // 3600
# n = n % 3600
# m = n // 60
# s = n % 60
#
# print(f'Дни: {d} ')
# print(f'Часы: {h} ')
# print(f'Минуты: {m} ')
# print(f'Секунды: {s} ')

# Тринадцатая задача

# n = int(input())
#
# d_1 = n // 1000
# d_2 = n // 100 % 10
# d_3 = n // 10 % 10
# d_4 = n % 10
# sum_d = d_1 + d_2 + d_3 + d_4
# mult_d =  d_1 * d_2 * d_3 * d_4
#
#
# print(f'Тысячи: {d_1}')
# print(f'Сотни: {d_2}')
# print(f'Десятки: {d_3}')
# print(f'Единицы: {d_4}')
# print(f'Сумма цифр: {sum_d}')
# print(f'Произведение цифр: {mult_d}')
# print(f'Обратный код: {str(d_4) + str(d_3) + str(d_2) + str(d_1)}')

# Четырнадцатая задача

# n_1 = int(input())
# n_2 = int(input())
# n_3 = int(input())
#
# p_1 = n_1 // 2 + n_1 % 2
# p_2 = n_2 // 2 + n_2 % 2
# p_3 = n_3 // 2 + n_3 % 2
# sum_p = p_1 + p_2 + p_3
#
# print(f'Первый класс: {p_1}')
# print(f'Второй класс: {p_2}')
# print(f'Третий класс: {p_3}')
# print(f'Всего парт: {sum_p}')

# Пятнадцатая задача

# n = int(input())
# k = int(input())
#
# f = (n + k - 1) // k
# p = (n - 1) % k + 1
#
#
# print(f'Этаж: {f}')
# print(f'Позиция на этаже: {p}')

# Шестнадцатая задача

# f = int(input())
# m = int(input())
#
# if f >= m:
#     print('Статус: ЗАПУСК РАЗРЕШЁН')
# else:
#     print('Статус: ЗАПУСК ЗАПРЕЩЁН')

# Семнадцатая задача

# n = int(input())
#
# if n % 2 == 0:
#     print('Сигнал: ЧЁТНЫЙ')
# else:
#     print('Сигнал: НЕЧЁТНЫЙ')

# Восемнадцатая задача

# n = int(input())
#
# if n < 0:
#     print('Положение: СЛЕВА')
# elif n > 0:
#     print('Положение: СПРАВА')
# else:
#     print('Положение: В БАЗЕ')

# Девятнадцатая задача

# g_1 = int(input())
# g_2 = int(input())
# g_3 = int(input())
#
# lider_counter = 1
# max_g = 0
#
#
# if g_1 > g_2:
#     max_g = g_1
# elif g_1 < g_2:
#     max_g = g_2
# elif g_1 == g_2:
#     max_g = g_1
#     lider_counter += 1
# if max_g < g_3:
#     max_g = g_3
#     lider_counter = 1
# elif max_g == g_3:
#     lider_counter += 1
#
# print(f'Максимальная мощность: {max_g}')
# print(f'Количество лидеров: {lider_counter}')

# max_g = int(input())
# cnt = 1
#
# for i in range(2):
#     g = int(input())
#     if g > max_g:
#         max_g = g
#         cnt = 1
#     elif g == max_g:
#         cnt += 1
#
# print(f'Максимальная мощность: {max_g}')
# print(f'Количество лидеров: {cnt}')

# Двадцатая задача

# n = int(input())
# r = ('')
#
# if n < -20:
#     r = ('ЭКСТРЕМАЛЬНЫЙ ХОЛОД')
# elif -20 <= n < 0:
#     r = ('ХОЛОДНО')
# elif 0 <= n < 20:
#     r = ('ПРОХЛАДНО')
# elif 20 <= n < 30:
#     r = ('КОМФОРТНО')
# else:
#     r = ('ЖАРКО')
#
# print(f'Режим: {r}')

# Двадцать первая задача

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print('Тип: РАВНОСТОРОННИЙ')
#     elif a != b != c != a:
#         print('Тип: РАЗНОСТОРОННИЙ')
#     elif a == b or b == c or c == a:
#         print('Тип: РАВНОБЕДРЕННЫЙ')
# else:
#     print('Тип: ТРЕУГОЛЬНИК НЕ СУЩЕСТВУЕТ')

# Двадцать вторая задача

# n = float(input())
#
# if (n) % 4 == 0 and (n) % 100 != 0 or (n) % 400 == 0 :
#     print('Год: ВИСОКОСНЫЙ')
# else:
#     print('Год: НЕВИСОКОСНЫЙ')

# Двадцать третья задача

# x = int(input())
# y = int(input())
#
# p = ('')
#
# if x > 0 and y > 0:
#     p = ('ПЕРВАЯ ЧЕТВЕРТЬ')
# elif x < 0 and y > 0:
#     p = ('ВТОРАЯ ЧЕТВЕРТЬ')
# elif x < 0 and y < 0:
#     p = ('ТРЕТЬЯ ЧЕТВЕРТЬ')
# elif x > 0 and y < 0:
#     p = ('ЧЕТВЁРТАЯ ЧЕТВЕРТЬ')
# elif x == 0 and y == 0:
#     p = ('НАЧАЛО КООРДИНАТ')
# elif y == 0:
#     p = ('ОСЬ X')
# elif x == 0:
#     p = ('ОСЬ Y')
#
# print(f'Положение: {p}')

# Двадцать третья задача

# start_column = int(input())
# start_line = int(input())
# end_column = int(input())
# end_line = int(input())
#
# if start_column == end_column and (start_line > end_line or start_line < end_line):
#     print('Ход: ВОЗМОЖЕН')
# elif start_line == end_line and (start_column > end_column or start_column < end_column):
#     print('Ход: ВОЗМОЖЕН')
# else:
#     print('Ход: НЕВОЗМОЖЕН')

# Двадцать четвертая задача

order_price = int(input())
distance = int(input())
cargo_mass = int(input())
is_urgent = int(input())

base_price = 0
surcharge = 0
total_price = 0

if order_price < 5000:
    if distance <= 5:
        base_price = 200
    elif distance <= 20:
        base_price = 400
    else:
        base_price = 700

if cargo_mass > 20:
    surcharge += 500
if is_urgent == 1:
    surcharge += 300

total_price = base_price + surcharge

print(f'Базовая стоимость: {base_price}',
      f'Доплата: {surcharge}',
      f'Итого: {total_price}', sep='\n')




