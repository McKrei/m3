import time

import schedule


def job():
   time.sleep(7)
   print("Работаю...")

def job1():
   print("Работаю 1")


schedule.every(5).seconds.do(job)
schedule.every(10).seconds.do(job1)


while True:
   schedule.run_pending()
   time.sleep(1)
