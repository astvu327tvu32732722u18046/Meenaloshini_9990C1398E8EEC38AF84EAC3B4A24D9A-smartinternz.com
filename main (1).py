# finding a leap year
year = int(input("enter the year:"))
if (year % 400 == 0 and year % 100 == 0) or (year % 4 == 0):
  print(year, "is a leap year ")
else:
  print(year, "is not a leap year ")
