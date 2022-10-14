# Oscar Jasso
# PSID : 1895743

import csv

# accept user input
csv_input = input()

# open and read csv file
# create list from the file
with open(csv_input, 'r') as file:
    csv_file = csv.reader(file)
    for line in csv_file:
        csv_list = line

# initiate new list
# loop through csv list and add words to new list only one time
    new_list = []
    for word in csv_list:
        if word not in new_list:
            new_list.append(word)

# loop through the new list and print out the word and its frequency found in the original csv list
    for w in new_list:
        word_count = csv_list.count(w)
        print(w, word_count)
