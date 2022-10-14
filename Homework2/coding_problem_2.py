# Oscar Jasso
# PSID : 1895743

# import datetime so you can load the current date.
import datetime

# create a dictionary with the months and corresponding number.
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

# set the current date to a variable and separate the month, day and year to compare later.
today = datetime.date.today()
today_month = today.month
today_day = today.day
today_year = today.year

# initiate and continue to ask for date one at a time until -1 is given
# as dates are entered append them to list to save them
input_date = input("Enter a Date: ")
dates = []
while input_date != '-1':
    dates.append(input_date)
    input_date = input("Enter a Date: ")

# iterate through dates in list, if date meets format requirements (have a ',') then append it to a new list.
# use find() method
new_dates = []
for n in dates:
    form_date = n.find(',')
    if form_date != -1:
        new_dates.append(n)

# iterate through dates in correct format list and split parts into month,day, year.
# ignores any month that isn't a key from the dictionary(wrong format)
# delete the ',' in day by replacing it with a blank space.
# make sure date is before the current date
# reformat and print date
for i in new_dates:
    split_date = i.split()
    month = months[split_date[0]]
    day = split_date[1].replace(',', '')
    year = split_date[2]
    if int(year) > today_year:
        break
    elif int(year) == today_year and int(month) > today_month:
        break
    elif int(year) == today_year and int(month) == today_month and int(day) > today_day:
        break
    else:
        date = f'{month}/{day}/{year}'
        print(date)
