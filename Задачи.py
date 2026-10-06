# h = int(input())
# m = int(input())
#
# price = 0
#
# if m >= 20:
#     price = 280 + (m-20)* 8
# elif 5 < m <= 19:
#     price = 100 + (m - 5) * 12
# else:
#     price = m * 20
#
# if 0 <= h < 6 or h >= 22:
#     price = price - price // 4
#
# print(price)

# p = input()
#
# p1 = ''
# p2 = ''
# p3 = ''
# p4 = ''
#
# for i in p:
#     if p1 == '':
#         p1 = i
#     elif p2 == '':
#         p2 = i
#     elif p3 == '':
#         p3 = i
#     else:
#         p4 = i
#
# p1 = int(p1)
# p2 = int(p2)
# p3 = int(p3)
# p4 = int(p4)
#
# if p1 == p2 == p3 == p4:
#     print('MASTER')
# elif p == p[::-1]:
#     print('MIRROR')
# elif (p2 - p1) == 1 and (p3 - p2) == 1 and (p4 - p3) == 1 or (p1 - p2) == 1 and (p2 - p3) == 1 and (p3 - p4) == 1:
#     print('LADDER')
# elif p1 == p2 or p2 == p3 or p3 == p4:
#     print('TWIN')
# else:
#     print('REJECT')


# b = int(input())
# w = int(input())
# v = int(input())
# d = int(input())
#
# if b < 10 or b < 20 and d > 500:
#     print('EMERGENCY')
# elif w > 25 or v < 100:
#     print('CLOSED')
# elif b >= 30 and w <= 12 and v >= 800:
#     print('AUTO')
# elif b >= 20 and w <= 20 and v >= 300:
#     print('MANUAL')
# else:
#     print('WAIT')

# h = int(input())
# d = int(input())
# s = int(input())
#
# if d == 0:
#     if h <= 2:
#         price = h * 80
#     elif h <= 5:
#         price = h * 60
#     else:
#         price = h * 40
# else:
#     if h <= 2:
#         price = h * 100
#     else:
#         price = h * 80
#
# if s == 1:
#     price = price - price // 4
#
# print(price)

# t = int(input())
# h = int(input())
# s = int(input())
#
# if s != 1:
#     if t < 10:
#         print('HEAT')
#     elif t > 30:
#         if h < 40:
#             print('MIST')
#         else:
#             print('COOL')
#     else:
#         if h < 30:
#             print('WATER')
#         elif h > 80:
#             print('VENT')
#         else:
#             print('HOLD')
# else:
#     print('ALARM')

'''Задача не принята'''
# o = int(input())
# b = int(input())
# s = int(input())
#
# if o == 2:
#     print('STOP')
# elif o == 1:
#     if s == 0 and b >= 40:
#         print('DETOUR')
#     else:
#         print('WAIT')
# else:
#     if  s == 1:
#         if b >= 30:
#             print('SLOW')
#         else:
#             print('CHARGE')
#     else:
#         if b >= 10:
#             print('GO')
#         else:
#             print('CHARGE')
'''-----------------------------'''
# s1 = input().split()
# s2 = input().split()
#
# q1, t1, b1 = int(s1[0]), int(s1[1]), int(s1[2])
# q2, t2, b2 = int(s2[0]), int(s2[1]), int(s2[2])
#
#
# if q1 > q2:
#     print('FIRST')
# elif q1 == q2:
#     if t1 < t2:
#         print('FIRST')
#     elif t1 == t2:
#         if b1 > b2:
#             print('FIRST')
#         elif b1 == b2:
#             print('DRAW')
#         else:
#             print('SECOND')
#     else:
#         print('SECOND')
# else:
#     print('SECOND')

# n = int(input())
#
# for i in range(n):
#     i += 1
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, 'BOTH')
#     elif i % 3 == 0:
#         print(i, 'BLUE')
#     elif i % 5 == 0:
#         print(i, 'RED')
#     else:
#         print(i, 'WHITE')

# s = input().split()
# n = int(s[0])
# l = int(s[1])
# r = int(s[2])
#
# cnt = 0
# m = 0
#
# for i in range(n):
#     x = int(input())
#     if l <= x <= r:
#         cnt += 1
#         m += x
#
# print(cnt, m)

# n = int(input())
#
# m = 121
# f = 0
# q = 0
#
# for i in range(1, n + 1):
#     x = int(input())
#     if x < m:
#         m = x
#         f = i
#         q = 1
#     elif x == m:
#         q += 1
# print(m, f, q)


# str = input().split()
# c = int(str[0]) # Вместимость
# s = int(str[1]) # Кол-во пассажиров
# n = int(str[2]) # Число операций
#
# d = 0 # Число отклоненных операций
#
# for i in range(1, n + 1):
#     x = int(input())
#     if s + x <= c and s + x >= 0:
#         s += x
#     else:
#         d += 1
# print(s, d)

# str = input().split()
# r = int(str[0]) # строки
# c = int(str[1]) # столбцы
#
# for i in range(1, r + 1):
#     for j in range(1, c + 1):
#         if i == 1 or j == 1 or i == r or j == c:
#             print('#', end='')
#         elif i == j:
#             print('*', end='')
#         elif (i + j) % 2 == 0:
#             print('.', end='')
#         else:
#             print(':', end='')
#     print()

# st = input().split()
# a = int(st[0]) # батарея А
# b = int(st[1]) # батарея В
# s = int(st[2]) # Необходимое количество энергии
# k = int(st[3]) # Ограничение по батареям
#
# x = 0
# y = 0
# m = k
# l = k
# if s == 0:
#     print(x ,y)
# else:
#     for i in range(k + 1):
#         for j in range(m + 1):
#             if a * i + b * j == s and i + j <= l:
#                 x = i
#                 y = j
#                 print(x, y)
#     m = m - 1
#
#     if x == 0 and y == 0:
#         print('NONE')

# st = input().split()
#
# r = int(st[0]) # ряды
# c = int(st[1]) # датчики
# t = int(st[2]) # температура
#
# mt = -51 # максимальная температура
# n_str = 0 # номер строки
# n_clm = 0 # номер столбца
# cnt = 0
#
# for i in range (1, r + 1):
#     # print('строки', i)
#     temp = input().split()
#     # print('temp', temp)
#     for k in range(len(temp)):
#         if int(temp[k]) >= t:
#             # print('k температура', int(temp[k]))
#             # print('температура порог', t)
#             cnt += 1
#         if int(temp[k]) > mt:
#             mt = int(temp[k])
#             n_str = i
#             n_clm = k + 1
#     print(cnt)
#     cnt = 0
# print(mt, n_str, n_clm)

# a = 0
# b = 0
#
#
# for i in range(1000):
#     x = int(input())
#     if x == 1:
#         a += 1
#     elif x == 2:
#         b += 1
#     else:
#         break
# print(a, b)

# e = int(input())
# t = int(input())
# g = int(input())
# d = int(input())
#
# days = 0
# cap = e
#
# while cap < t:
#     cap += g
#     days += 1
#     if cap >= t:
#         break
#     else:
#         cap -= d
#
# print(days, cap)

n = input()
z_cnt = 0

print(len(n), end=' ')

for i in range(len(n)):
    if n[i] == '0':
        z_cnt += 1
        print(z_cnt, end=' ')



s = []
for i in range(len(n)):
    s.append(n[i])

print(max(s), end=' ')

while len(s) > 1:
    s.pop()
print(len(s), end=' ')


total = 0
sign = 1

while n > 0:
    ld = n % 10
    n = n // 10
    total = 0
    sign = 1






































