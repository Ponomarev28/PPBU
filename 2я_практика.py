# A. Грузовые капсулы

# n = int(input())
# k = int(input())
# b = int(input())
# p = int(input())
#
# capsule_count = 0
# space_count = 0
# energy_consumption = 0
#
# space_count = n % k
# capsule_count = n // k
#
# if space_count != 0:
#     capsule_count += 1
#     space_count = k - space_count
#
# energy_consumption = capsule_count * b + n * p
#
#
# print(capsule_count, space_count, energy_consumption, sep='\n')

# B. Поправка орбитальных часов

# h = int(input())
# m = int(input())
# s = int(input())
# d = int(input())
#
# sec_in_day = 86400
#
# t = h * 3600 + m * 60 + s
# t = t + d
#
# sutki = t // sec_in_day
# t = t % sec_in_day
# h = t // 3600
# t = t % 3600
# m = t // 60
# s = t % 60
#
# print(sutki, h, m, s)

# Шлюз полярной станции

p = int(input())
a = int(input())
c = int(input())
r = int(input())

if a == 1:
    print('LOCKDOWN')
elif p == 0:
    print('NO_PASS')
elif c < r:
    print('DENIED')
else:
    print('ACCESS')









