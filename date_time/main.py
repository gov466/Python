import calendar  #importing modules for using in this program
import datetime

print(calendar.weekheader(2)) #prints day names
print()

print(calendar.month(2020,5,3)) #prints may 2020 with weekheadr 3
print()
print(calendar.monthcalendar(2020,5)) #prints in matrix format
print()
print(calendar.calendar(2020)) ##whole yr
day_of_week =calendar.weekday(2020,5,1) #prints  day of the week
print(day_of_week)
is_leap=calendar.isleap(2020)
print(is_leap)
how_many_leap_days =calendar.leapdays(2000,2020)
print(how_many_leap_days)

date_time= datetime.datetime.now()    #displays current date and time now
print(date_time)
print()             #just a blank line
date= datetime.date.today() #displays current date
print(date)
