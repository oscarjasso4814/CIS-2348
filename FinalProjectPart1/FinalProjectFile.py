# Oscar Jasso
# PSID : 1895743

# Import csv module.
# Import datetime module.
import csv
import datetime

# Use the date time model to set the current month, day, and year to a variable for later use.
today = datetime.date.today()
today_month = today.month
today_day = today.day
today_year = today.year

# Opens and reads the manufacturer list.
# Use csv reader to read each line of csv file.
# Loop through all the lines in file and use index to name each value.
# Creates a dictionary with list of manufacturer, type and damages values and item id as key for easy lookup.
man_dict = {}
with open("ManufacturerList.csv", "r") as manufacturer_file:
    csv_reader_man_file = csv.reader(manufacturer_file)
    for line in csv_reader_man_file:
        item_id = line[0]
        man_name = line[1]
        item_type = line[2]
        damage = line[3]
        if line[0] not in man_dict:
            man_dict[item_id] = [man_name, item_type, damage]

# Opens and reads the price list.
# Use csv reader to read each line of csv file.
# Loop through all the lines in file and creates a dictionary with item id as key and price value for easy lookup.
price_dict = {}
with open("PriceList.csv", "r") as price_file:
    csv_reader = csv.reader(price_file)
    for line in csv_reader:
        if line[0] not in price_dict:
            price_dict[line[0]] = line[1]

# Opens and reads the service date list.
# Use csv reader to read each line of csv file.
# Loop through all the lines in file and creates a dictionary with item id as key and date as value for easy lookup.
service_dict = {}
with open("ServiceDatesList.csv", "r") as service_file:
    csv_reader = csv.reader(service_file)
    for line in csv_reader:
        if line[0] not in service_dict:
            service_dict[line[0]] = line[1]

# Creates a list of the item ids.
# Set list to a variable.
# Sorts the item id list.
ordered_ids = man_dict.keys()
ordered_ids.sort()

# Open the csv file that will be written in.
# Call for it to be written in with csv method.
# Loop over the list of ordered ids and use the id to call its info from the manufacturer,
# Price and service date dictionaries.
# Set necessary info to a variable.
# Place the variables in the right order into a list.
# Place manufacturer name at front of list in order to use it later.
# Append the variable lists into the inventory list in order to create list of lists.


def get_full_inventory():
    inventory = []
    f = open('FullInventory.csv', 'w')
    writer = csv.writer(f)
    for i in ordered_ids:
        item_row = man_dict[i]
        price = price_dict[i]
        service_date = service_dict[i]
        manufacturer_name = item_row[0]
        category = item_row[1]
        damages = item_row[2]
        if damages != '':
            line2 = [manufacturer_name, i, manufacturer_name, category, price, service_date, damages]
            inventory.append(line2)
        else:
            line2 = [manufacturer_name, i, manufacturer_name, category, price, service_date]
            inventory.append(line2)

# Sort the list by manufacturer name
# Get rid of the manufacturer name in the lists index 0
# Write the row of values into the opened csv file.
    inventory.sort()
    for row in inventory:
        del row[0]
        writer.writerow(row)

# Create a list for all the item types for later use.
# Create a list for all csv file names for later use.
# Create a dictionary with item types as key and list of ids for values.


def get_item_inventories():
    type_list = []
    csv_type_list = []
    type_dict = {}

# Loop over item ids in ordered list.
# Use the item ids to get that items row of values.
# Get the capitalized item type for each item and set it to a variable.
# Append that capitalized item typ to a list for later use.
    for x in ordered_ids:
        row = man_dict[x]
        i_type = (row[1]).capitalize()
        if i_type not in type_list:
            type_list.append(i_type)

# Create a dictionary with item types as key and a blank list as value for later use.
    for x in type_list:
        type_dict[x] = []

# Loop over the list of ordered ids and use the id to call its item type info from the manufacturer dictionary.
# Place the item id into the list under the matching item type key value.
    for x in ordered_ids:
        row = man_dict[x]
        i_type = (row[1]).capitalize()
        if i_type in type_dict:
            type_dict[i_type].append(x)

# Loop over the types list.
# Create a capitalized csv file name for each item type in the list.
# Put these csv file names in a list.
    for types in type_list:
        csv_type_list.append('{}Inventory.csv'.format(types.capitalize()))

# Create a dictionary with types as key and capitalized csv name as value.
    csv_type_dict = {}
    for x in csv_type_list:
        type_name = x.split('Inventory')
        type_name = type_name[0]
        csv_type_dict[type_name] = x

# Loop through type list.
# Use the item type to call information from type dictionary and csv type dictionary and set them to a variable.
# Open csv file to write in using variable as name.
# Loop through type dictionary to access rows with item information.
# Write the row of values into the opened csv file.

    for x in type_list:
        lists = type_dict[x]
        i = csv_type_dict[x]
        f = open(i, 'w')
        writer = csv.writer(f)
        print(x)
        for t in lists:
            row = man_dict[t]
            price = price_dict[t]
            service_date = service_dict[t]
            manufacturer = row[0]
            damages = row[2]

            if damages != '':
                k = (t, manufacturer, price, service_date, damages)
                writer.writerow(k)
                print(k)
            else:
                k = (t, manufacturer, price, service_date)
                writer.writerow(k)
                print(k)

# Open the csv file that will be written in.
# loop over ordered list of item ids.
# Use those ids to call information and set to a variable.
# Split the service date and set month, day , and year variable.


def get_past_service_date():
    dates_dict = {}
    f = open('PastServiceDateInventory.csv', 'w')
    writer = csv.writer(f)
    serviced_inventory = []
    for x in ordered_ids:
        row = man_dict[x]
        price = price_dict[x]
        service_date = service_dict[x]
        manufacturer = row[0]
        damages = row[2]
        i_type = row[1]
        split_date = service_date.split("/")
        service_month = split_date[0]
        service_day = split_date[1]
        service_year = split_date[2]

# Compare the current day to service date of the item.
# If service date is has already past based on current day add it to past service day list, if not do nothing
        if int(service_year) > today_year:
            continue
        elif int(service_year) == today_year and int(service_month) > today_month:
            continue
        elif int(service_year) == today_year and int(service_month) == today_month and int(service_day) > today_day:
            continue
        else:
            if damages != '':
                s = [service_year, x, manufacturer, i_type, price, service_date, damages]
                serviced_inventory.append(s)
                dates_dict[service_date] = [s]
            else:
                s = [service_year, x, manufacturer, i_type, price, service_date]
                serviced_inventory.append(s)
                dates_dict[service_date] = [s]
# Sort the list by service date.
# Get rid of the first service date value.
# Write the row of values into the opened csv file.

    serviced_inventory.sort()
    for x in serviced_inventory:
        del x[0]
        writer.writerow(x)


# Open the csv file that will be written in.
# loop over ordered list of item ids.
# Use those ids to call information and set to a variable.
# If damage variable is not empty add list of info to damaged item list with price as first object.


def get_damaged():
    f = open('DamagedInventory.csv', 'w')
    writer = csv.writer(f)
    damaged_item_list = []

    for x in ordered_ids:
        row = man_dict[x]
        price = price_dict[x]
        service_date = service_dict[x]
        manufacturer = row[0]
        type_item = row[1]
        damages = row[2]

        if damages != "":
            item_info = [price, x, manufacturer, type_item, price, service_date]
            damaged_item_list.append(item_info)

# Sort the list of lists by price from lowest to greatest
    damaged_item_list.sort(reverse=True)

# For each group of info in damaged item list delete the first price object
# Write the line into the csv file.
    for group in damaged_item_list:
        del group[0]
        writer.writerow(group)


get_full_inventory()
get_item_inventories()
get_past_service_date()
get_damaged()
