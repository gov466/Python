import datetime
import pytz ##timezone
today= datetime.date.today()
print(today) #cuurent date

birthday= datetime.date(1995,12,4)
print(birthday) #brithdays

days_since_birth= (today -birthday).days
print(days_since_birth) ##birth since days

tdelta=datetime.timedelta(days=10)
print(today+tdelta) ##add 10 to todays date

tdelta=datetime.timedelta(days=10)
print(today-tdelta) ##minus 10days

print(today.day)
print(today.month) 
print(today.weekday()) ##momday=0 tue=1...

print(datetime.time(7,2,20,15))
 #datetime.date(y,m,d)
 #datetime.time(h,m,s,ms)
 #datetime.datetime(y,m,d,h,m,s,ms)
print(datetime.datetime.now()) #current day and time

#10hours to current day
hour_delta = datetime.timedelta( hours=10)
print(datetime.datetime.now()+hour_delta)
 
datetime_today=datetime.datetime.now(tz=pytz.UTC)
datetime_pacific =datetime_today.astimezone(pytz.timezone('US/pacific'))
print(datetime_pacific)

#for tz in pytz.all_timezones:
 # print(tz) ##prints alll time zones

  #string formatting with date
  #2020/05/14 -->may 15 2020
  #strftime(f=formatting)
print(datetime_pacific.strftime('%B %d %Y')) ##date in string format

#march 09,2019 ->2020/05/14
#strptime(p=parsing)
datetime_thing= datetime.datetime.strptime('May 14,2020','%B %d, %Y')
print(datetime_thing)
