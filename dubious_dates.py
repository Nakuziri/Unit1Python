##Making 3 different imports from the "datetime" module 
from datetime import date, time, datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
#prints current date and time
print(datetime.now())

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
#giving current date & time a variable
x= (datetime.now())

#prints month, day ,year and hours to seconds
print(x.strftime('%m/%d/%y %H:%M:%S'))
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
day1 = '10 12 2023'
day2 = '09 01 2023'

day1 = datetime.strptime(str_day1, "%Y/%m/%d") 
day2 = datetime.strptime(str_day2, "%Y/%m/%d")
timeing = day2 - day1
print(f 'Difference is {timing.days} days')


"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
