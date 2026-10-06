'''Цикл while'''

i = 0

while i < 10:
    i += 1
    if i == 17:
        break
    print(i, end=' ')
else:
    print('\nOK')


 # АЛГОРИТМ --- Обработка числовой последовательности ---

# n = int(input('> '))
# sm = 0
# cnt = 0
#
# while n != 0:
#     sm += n
#     cnt += 1
#     n = int(input('> '))
# print(f'Сумма - {sm}\n'
#       f'Количесвто - {cnt}')

# АЛГОРИТМ --- парсер чисел ---

# n = int(input('> '))
#
# nn = n
# sm = 0
# cnt = 0
#
# while n > 0:
#     rem = n % 10
#     sm += rem
#     cnt += 1
#     n //= 10
# print(f'В числе {nn} {cnt} ц., суммой {sm}')