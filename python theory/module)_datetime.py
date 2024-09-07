
import datetime as dt 
print(dt.datetime.now())

print(dt.datetime(2024,3,18))
# creating date objects

now = dt.datetime.now()
year = now.strftime("%Y")

print("YEAR ",year)
