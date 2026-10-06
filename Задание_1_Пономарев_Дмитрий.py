'''Задание №1'''

# Решение первой задачи

i = 3
while True:
    print(i)
    if i + 10 > 43:
        break
    i += 10

# Решение второй задачи

i = input('Введите пароль: ')

while True:
    if len(i) >= 8:
        print('OK')
        break
    else:
        print('Пароль меньше 8 символов')
    i = input('Введите пароль: ')

# Решение третей задачи

text = input('Введите параметры автомобиля по шаблону: ')
mark = (' ')
year = (' ')
mileage = (' ')
price = (' ')
start = 0
field = 0

for i in range(len(text)):
    if text[i] == ' ':
        if field == 0:
            mark = text[start:i]
        elif field == 1:
            year = text[start:i]
        elif field == 2:
            mileage = text[start:i]
        field += 1
        start = i + 1
        if field == 3:
            break
price = text[start:]

print(f'Продается автомобиль\nМарка: {mark}\nГод выпуска: {year}\nПробег: {mileage}\nЦена: {price}')
























