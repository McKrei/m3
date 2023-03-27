import datetime

    # Создание объекта datetime с текущей датой и временем:


now = datetime.datetime.now()
print(now)

    # Создание объекта datetime с определенной датой и временем:



dt = datetime.datetime(2023, 3, 27, 12, 30, 0)
print(dt)

    # Использование метода strftime() для форматирования даты и времени:


dt = datetime.datetime(2023, 3, 27, 12, 30, 0)
print(dt.strftime("%Y-%m-%d %H:%M:%S"))

    # Использование объекта timedelta для вычисления разницы между двумя датами:


dt1 = datetime.datetime(2023, 3, 27, 12, 30, 0)
dt2 = datetime.datetime(2023, 3, 28, 14, 0, 0)
diff = dt2 - dt1
print(diff)

    # Использование объекта timedelta для добавления или вычитания времени от даты:

dt = datetime.datetime(2023, 3, 27, 12, 30, 0)
delta = datetime.timedelta(days=1, hours=3)
new_dt = dt + delta
print(new_dt)

































