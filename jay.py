from datetime import datetime
from datetime import time
from datetime import datetime, date
from datetime import timedelta

now = datetime.now()
print (now.time())
t2 = timedelta(hours = 14, minutes = 19)
timestr = datetime.now()
Check_TIMEnow = timestr.strftime("%H:%M")
print (Check_TIMEnow)
data =[]
dt = datetime.datetime.today()
print(dt)
for i in range(1):
    delta = datetime.timedelta(minutes = i)
    dtnew = dt + delta
    data.append(str(dtnew))
print(data)

#I tried ot append the current time inot a list and compare the two, but it didnt work
