#1
import datetime
x=datetime.datetime.now()
five_days_ago=x-datetime.timedelta(days=5)
print(five_days_ago)


#2
import datetime
x=datetime.datetime.today()
yesterday=x-datetime.timedelta(days=1)
tomorrow=x+datetime.timedelta(days=1)
print(x)
print(yesterday)
print(tomorrow)


#3
import datetime 
x=datetime.datetime.today()
now=x.replace(microsecond=0)
print(now)


#4
from  datetime import datetime
date1=datetime(2024,9,21,14,30)
date2=datetime(2024,9,28,16,50)
different=date2-date1
print(different)

