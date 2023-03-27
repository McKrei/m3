

import datetime
import time

# import schedule


# 17.12.2023

# Пример вывода:
# 17.12.2023
# 23.12.2023
# 24.12.2023
# 30.12.2023
# 31.12.2023


# date = datetime.datetime.strptime(input(), '%d.%m.%Y')

# year = date.year
# while year == date.year:
#    if date.isoweekday() in [6, 7]:
#        print(date.strftime('%d.%m.%Y'))
#    date += datetime.timedelta(days=1)



# Пример ввода:
# 4 2023

# Пример вывода:
# пн	вт	ср	чт	пт	сб	вс
# 					1	2
# 3	4	5	6	7	8	9
# 10	11	12	13	14	15	16
# 17	18	19	20	21	22	23
# 24	25	26	27	28	29	30



# weekdays = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']

# date = datetime.datetime.strptime('3 2023', '%m %Y')
# month = date.month
# print(*weekdays, sep='\t', end='\t')
# print()
# print('\t' * date.weekday(), end='')
# while month == date.month:
#    print(date.day, end='\t')
#    if date.isoweekday() == 7:
#        print()
#    date += datetime.timedelta(days=1)
# print()


# Пример ввода:
# 2
# 1.2.2023

# Пример вывода:
# 04.02.2023
# 04.03.2023
# 12.03.2023
# 18.03.2023




total = 0
max_count = 3
count = int(input())
date = datetime.datetime.strptime(input(), '%d.%m.%Y')

while total < 4:
    if count < max_count:
        if date.isoweekday() in [6, 7] and date.day % 2 == 0:
            print(date.strftime('%d.%m.%Y'))
            total += 1
            count += 1
        date += datetime.timedelta(days=1)
    else:
        date = datetime.datetime(date.year, date.month + 1, 1)
        count = 0




def print_time():
    now_date = datetime.datetime.now()
    new_year = datetime.datetime(now_date.year, 12, 31)
    delta = new_year - now_date
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60
    print(f'До нового года осталось дней: {days}, часов: {hours}, минут: {minutes}, секунд: {seconds}.')

schedule.every().seconds.do(print_time)

while True:
    schedule.run_pending()
    time.sleep(1)
