# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input("Enter the month of the year (Jan - Dec): ").lower()
day = int(input("Enter the day of the month: "))
if month in ('dec', 'jan', 'feb'):
  season = 'winter'
elif month in ('mar', 'apr', 'may'):
  season = 'spring'
elif month in ('jun', 'jul', 'aug'):
  season = 'summer'
elif month in ('sep', 'oct', 'nov'):
  season = 'fall'
if month == 'dec' and day >= 21:
  season = 'winter'
elif month == 'mar' and day <= 19:
  season = 'winter'
elif month == 'mar' and day >= 20:
  season = 'spring'
elif month == 'jun' and day <= 20:
  season = 'spring'
elif month == 'jun' and day >= 21:
  season = 'summer'
elif month == 'sep' and day <= 21:
  season = 'summer'
elif month == 'sep' and day >= 22:
  season = 'fall'
elif month == 'dec' and day <= 20:
  season = 'fall'
print(month, day, 'is in', season)


