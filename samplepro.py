import datetime
from datetime import date
import calendar

def day(date):
    year, month, day = (int(i) for i in date.split('-'))
    dy = datetime.date(year, month, day)
    return dy.strftime("%A")

today=date.today()
strin=str(today)
mstr= "Have a Nice "+day(strin)+" !!! "
print(" "*25 + mstr)


