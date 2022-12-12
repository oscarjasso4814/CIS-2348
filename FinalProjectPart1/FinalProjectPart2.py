# Oscar Jasso
# PSID : 1895743

# Import csv module.
# Import datetime module.
import csv
import datetime

# Use the date time model to set the current month, day, and year to a variable for later use.
# initiate a variable for day, month, and year for service date of item.
today = datetime.date.today()
today_month = today.month
today_day = today.day
today_year = today.year
service_month = None
service_day = None
service_year = None
consider_month = None
consider_day = None
consider_year = None

# Opens and reads the price list.
# Use csv reader to read each line of csv file.
# Loop through all the lines in file and creates a dictionary with item id as key and price value for easy lookup.
price_dict = {}
with open("PriceList.csv", "r") as price_file:
    csv_reader = csv.reader(price_file)
    for line in csv_reader:
        if line[0] not in price_dict:
            price_dict[line[0]] = line[1]

# initialize a list for items (manufacturer and type)
# initialize a list of manufacturers that exist in csv file.
# initialize list of item types that exist in csv file.
# initialize a dictionary with list of manufacturer, type and damages values and item as key for easy lookup.
# initialize a dictionary with list of manufacturer, type and damages values and item id as key for easy lookup.
# initialize a dictionary with list of item ids and corresponding types as key for easy lookup.
item_list = []
existing_man_list = []
existing_type_list = []
man_dict = {}
id_dict = {}
type_dict = {}


# Opens and reads the manufacturer list.
# Use csv reader to read each line of csv file.
# Loop through all the lines in file and use index to name each value.
with open("ManufacturerList.csv", "r") as manufacturer_file:
    csv_reader_man_file = csv.reader(manufacturer_file)
    for line in csv_reader_man_file:
        item_id = line[0]
        man_name = line[1].lower()
        item_type = line[2].lower()
        damage = line[3]
        man_type = "{} {}".format(man_name, item_type)
# add an item to list of items (manufacturer and type)
        if man_type not in item_list:
            item_list.append(man_type)
# add manufacturer name to a list of manufacturers if it exists in csv file.
        if man_name not in existing_man_list:
            existing_man_list.append(man_name)
# add item type to a list of item types if it exist in csv file.
        if item_type not in existing_type_list:
            existing_type_list.append(item_type)
# fill a dictionary with list of manufacturer, type and damages values and item as key for easy lookup.
        if man_type not in man_dict:
            man_dict[man_type] = [item_id, man_name, item_type, damage]
# fill a dictionary with list of manufacturer, type and damages values and item id as key for easy lookup.
        if item_id not in id_dict:
            id_dict[item_id] = [item_id, man_name, item_type, damage]
# Creates a dictionary key with a blank list if item type not already in dictionary.
        if item_type not in type_dict:
            type_dict[item_type] = []
# fill the type dictionary with corresponding item ids.
        if item_type in type_dict:
            type_dict[item_type].append(item_id)

# Opens and reads the service date list.
# Use csv reader to read each line of csv file.
# Loop through all the lines in file and creates a dictionary with item id as key and date as value for easy lookup.
service_dict = {}
with open("ServiceDatesList.csv", "r") as service_file:
    csv_reader = csv.reader(service_file)
    for line in csv_reader:
        if line[0] not in service_dict:
            service_dict[line[0]] = line[1]

# initialize a list for the desired manufacturer.
# initialize a list for the desired item type.
# initialize a variable for the query.
# initialize a variable to hold the desired item.
# initialize a variable for the cost of the item.
input_man_list = []
input_type_list = []
query = None
desired_item = None
cost = None
query_list = []
# ask for input until user types 'q'.
while query != "q":
    query = raw_input("Enter the manufacturer and item type (Type 'q' to Quit): ")
    print('')
# quit once user types 'q'.
    if query == "q":
        print("You Have Quit, Farewell :)")
        break
# take input and make a list of lowercase words.
# if word exists in the manufacture or type list add it to the input lists.

    else:
        query_list = query.lower().split(" ")
        for word in query_list:
            if word in existing_man_list:

                input_man_list.append(word)
                continue
            if word in existing_type_list:
                input_type_list.append(word)

# if the input contained only one type and one manufacturer name your desired item
# if the input contains more than one type and manufacturer or none, the desired item doesnt exist
        if len(input_man_list) == 1 and len(input_type_list) == 1:
            desired_item = ("{} {}".format(input_man_list[0], input_type_list[0]))

        else:
            desired_item = None
            input_type_list = []
            input_man_list = []
# if the desired item does not exist in item list, print something.
        if desired_item not in item_list:
            print("No such item in inventory")
            print('')
            continue
# if desired item exists iin item list continue with finding its details.
# use the desired item as key to get its info from manufacturer dictionary.
#  set all necessary item info to a variable for later use.
        else:
            item_details = man_dict[desired_item]

            item_id = item_details[0]
            man_name = item_details[1]
            item_type = item_details[2]
            damage = item_details[03]
            cost = price_dict[item_id]
            service_date = service_dict[item_id]
            split_date = service_date.split("/")
            service_month = split_date[0]
            service_day = split_date[1]
            service_year = split_date[2]

# compare service date to current date, if service date was before today no good and print notification
        if int(service_year) < today_year:
            print("No such item in inventory")
            print('')
            input_man_list = []
            input_type_list = []
        elif int(service_year) == today_year and int(service_month) < today_month:
            print("No such item in inventory")
            print('')
            input_man_list = []
            input_type_list = []
        elif int(service_year) == today_year and int(service_month) == today_month and int(service_day) < today_day:
            print("No such item in inventory")
            print('')
            input_man_list = []
            input_type_list = []
# if the service date of item after today, check if not damaged then print.
        else:
            if damage == '':
                print("Your item is: {} {} {} {} ${}".format(item_id, man_name.capitalize(), item_type, damage, cost))
                print('')
                input_man_list = []
                input_type_list = []

# if item found find items with same type in type dictionary.
                line = type_dict[item_type]
# loop over ids, if id not damaged
                for considerId in line:
                    details = id_dict[considerId]
                    damaged = details[3]
                    service_date = service_dict[considerId]
                    split_date = service_date.split("/")
                    consider_month = split_date[0]
                    consider_day = split_date[1]
                    consider_year = split_date[2]
                    if int(consider_year) < today_year:
                        continue
                    elif int(consider_year) == today_year and int(consider_month) < today_month:
                        continue
                    elif int(consider_year) == today_year and int(consider_month) == today_month and int(
                            consider_day) < today_day:
                        continue
                    elif considerId != item_id and damaged == '':
                        ids = details[0]
                        name = details[1]
                        types = details[2]
                        price = price_dict[considerId]

                        print("You may also consider: {} {} {} ${}".format(ids, name.capitalize(), types, price))
                        print('')
# if damaged print notice.
            else:
                print("No such item in inventory")
                print('')
                input_man_list = []
                input_type_list = []

