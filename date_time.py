from datetime import date
from datetime import timedelta, date
import datetime

tdy = date.today()

yest = date.today() - timedelta(days=1)

tmr = date.today() + timedelta(days=1)

print("Today is ", tdy)
print("Yesterday was", yest)
print("Yesterday was", tmr)

print("\n", "#" *30, "\n")

current_time = datetime.datetime.now()
year = current_time.year
month = current_time.month
day = current_time.day
hour = current_time.hour
minute = current_time.minute
second = current_time.second

print("Current Time :  ", current_time)
print("Current Year :", year)
print("Month : ", month)
print("Day : ", day)
print("Hour : ", hour) 
print("Minute : ", minute) 
print("Second :", second)
 


