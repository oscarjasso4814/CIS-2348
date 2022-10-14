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


# open and read through the file
# create list from the data
my_file = open("inputData.txt", "r")
data = my_file.read()
dates = data.split("\n")

# iterate through dates in list, if date meets format requirements (have a ',') then append it to a new list.
# use find().
new_dates = []
for i in dates:
    find_comma = i.find(',')
    if find_comma != -1:
        new_dates.append(i)

# iterate through dates in new_dates list and split info into parts.
# ignores any month that isn't a key from the dictionary(wrong format),cant be called.
# delete the ',' in month by replacing it with a blank space.
# make sure date is before the current date.
# reformat and print date.
for x in new_dates:
    split_date = x.split()
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
