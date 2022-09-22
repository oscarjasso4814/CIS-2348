
# Oscar Jasso
# PSID : 1895743

# print out title
print("Birthday Calculator")

# ask for current month, day and year inputs and assign to variables
print("Current Day")
current_month = int(input('Month(#):\n'))
current_day = int(input('Day(#):\n'))
current_year = int(input('Year(#):\n'))

# ask for birthday month, day and year inputs and assign to variables
print('Birthday')
birthday_month = int(input('Month(#):\n'))
birthday_day = int(input('Day(#):\n'))
birthday_year = int(input('Year(#):\n'))

# subtract current year and birth year to get age

age = current_year - birthday_year

# create parameters for age before birthday
if current_month < birthday_month:
    age = age - 1
elif current_month == birthday_month and current_day < birthday_day:
    age = age - 1
else:
    age = current_year - birthday_year

# print statement
print("Birthday Calculator")
print("Current Day")
print(f'Month: {current_month}')
print(f'Day: {current_day}')
print(f'Year: {current_year}')
print('Birthday')
print(f'Month: {birthday_month}')
print(f'Day: {birthday_day}')
print(f'Year: {birthday_year}')
print('')
print(f'You are {age} years old.')

# IF birthday = current day and birth month == current month print a statement
if current_month == birthday_month and current_day == birthday_day:
    print("Happy Birthday!")

