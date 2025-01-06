# dates and times

import datetime

# date = datetime.date(2025,1,20)
# print(date)

# today = datetime.date.today()
# print(today)

# time = datetime.time(12,40,1)
# print(time)

# now = datetime.datetime.now()

# now = now.strftime("%H:%M:%S %d-%m-%Y")
# print(now)

target = datetime.datetime(2025,1,6,3,48,41)
current = datetime.datetime.now()

if target == current :
    print("target met")
else:
    print("not passed")