import calendar
generalCalendar = calendar.calendar(2021)
octoberCalendar = calendar.month(2021,1,3)
print(generalCalendar)
print(octoberCalendar)

#Regular Expressions
import re
details = 'My name is John Solomon jolomonson@gmail.com 18 years old.'
pattern = re.compile("[a-zA-Z0-9\,._-]+@[a-zA-Z0-9\,._-]+\.[a-zA-Z0-9\,._-]+")
result = pattern.search(details)
print(result)
