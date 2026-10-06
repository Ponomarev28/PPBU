from datetime import datetime, date, time, timedelta

# d = date(2024, 12, 31)
# t = time(12, 31, 16)
# print(d)
# print(t)
#
# dt = datetime.combine(d, t)
# print(dt, type(dt))
#
# d = date.today()
# print(d)
# dt = datetime.now().replace(microsecond=0)
# print(dt)
# # dt = dt.replace(year=2020, month=10, day=31)
# print(dt)
# dtt = input('Введите дату (дд.мм.гггг):')
# datte = datetime.strptime(dtt, '%d.%m.%Y')
# print(datte)
# print(datte.strftime('%A %d. %B. %Y %I:%m%p'))
# dt = datetime.now().replace(microsecond=0)
# dtt = dt.timetuple()
# for i in dtt:
#     print(i)

birthday = input('Введите дату (дд.мм.гггг):')
birthday = datetime.strptime(birthday, '%d.%m.%Y').date()
dt_now = date.today()
year_ = dt_now.year
birthday = birthday.replace(year=year_)
print(birthday, dt_now, year_)
if birthday < dt_now:
    birthday = birthday.replace(year=year_ + 1)
res = birthday - dt_now
if res.days == 0:
    print('С днем рождения!!!')
else:
    print(f'До Вашего дня рождения осталось {res.days} д.')

