# python dates
from datetime import date, timedelta

today = date.today()
print(today.month)
print(today.day)
print(today.year)
print(today.weekday)


f_date =today.strftime("%d/%m/%Y")
print(f_date)


# subscribtion
expiry_date = today + timedelta(days=30)
print(expiry_date)




date1 = date(2005, 1, 16)
date2 = date(1998, 12, 25)
diff = date1 - date2
print(diff.days)



