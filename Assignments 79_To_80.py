# 1
import datetime
Date = datetime.datetime(2021,6,25)
toDay = datetime.datetime.now()
dayDiff = (toDay - Date).days
print(f"Days From {Date } To {toDay} Is {dayDiff}")



print('-' *120)

# 2
print(toDay.strftime("%Y ,%A ,%d"))
print(toDay.strftime("%B %d ,%Y"))
print(toDay.strftime("%B /%d /%y"))
print(toDay.strftime("%d / %B / %Y"))         
print(toDay.strftime("%a, %d %B %Y"))  

print('-' *120)

# 3


print("-" * 100)

# 4

