''' Задачи '''

''' Задача A '''

# st = input().split()
#
# b = int(st[0])
# a = int(st[1])
# c = int(st[2])
#
# total = b + a - c
# print(total)


# a, b, c = list(map(int, input().split())) # сразу принять списком

''' Задача B '''

# x = 0
# y = 0
# st = input().split()
#
# a = int(st[0])
# b = int(st[1])
# c = int(st[2])
#
# y = b
# x = a - c
# s = a + b + c
#
# print(x, y, s)

''' Задача С '''

# st = input().split()
#
# x = int(st[0])
# y = int(st[1])
# cnt = 0
#
# while x != 0 and y != 0:
#     if x > 0:
#         x -= 1
#         cnt += 1
#     elif x < 0:
#         x += 1
#         cnt += 1
#
# while y != 0:
#     if y > 0:
#         y -= 1
#         cnt += 1
#     elif y < 0:
#         y += 1
#         cnt += 1
#
# print(cnt)

''' Задача D '''

# b, s, t = map(int, input().split())
# kit = min([b // 1, s // 2, t // 3])
# print(kit)


''' Задача E '''

# b, p = map(int, input().split())
# if b >= p:
#     print('YES')
# else:
#     print('NO')

''' Задача F '''

# a, b, k = map(int, input().split())
#
# r = abs(a - b)
#
# if r > k:
#     print('FLAG')
# else:
#     print('OK')

''' Задача G '''

# x1, y1, x2, y2 = map(int, input().split())
#
# if x1 == x2 and y1 == y2:
#     print('YES')
# else:
#     print('NO')

''' Задача G '''

# n = int(input())
# st = list(map(int, input().split()))
#
# if n == 1:
#     print(st[0], st[0])
# else:
#     print(st[0], st[-1])

''' Задача I '''

# input()
# a = list(map(int, input().split()))
#
#
# for i in range (len(a)):
#     if i == 0 or i % 2 == 0:
#         print(a[i], end=' ')



''' Задача K '''

# input()
# a = list(map(int, input().split()))
# was_1 = False
# for i in range(len(a)):
#     if a[i] == 1:
#         was_1 = True
#         print(i)
#         break
# if not was_1:
#     print(-1)

''' Задача 3 '''

# a = list(map(int, input().split()))
#
# b = int(a[0])
# p = int(a[1])
# cnt = b // p
# r = b % p

''' Задача 6 '''

# a = list(map(int, input().split()))
#
# b = int(a[0])
# s = int(a[1])
# t = int(a[2])
#
#
# s2 = s // 2
# t2 = t // 3
#
# b3 = b % 1
# s3 = s % 2
# t3 = t % 3
#
# print(min(b, s2, t2))

list1 = list(map(int, input().split()))
list2 = (1, 2, 3)

print(list1)
print(list2)











