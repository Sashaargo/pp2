1.
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)

2.
from datetime import date, timedelta
yesterday = date.today() - timedelta(1)
tomorrow = date.today() + timedelta(1)
print('yesterday :',yesterday)
print('today :',date.today())
print('tomorrow :',tomorrow)

3.
import datetime
dt = datetime.datetime.today().replace(microsecond=0)
print(dt)

4.
from datetime import datetime, time
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
date1 = datetime.strptime('2024-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
print()