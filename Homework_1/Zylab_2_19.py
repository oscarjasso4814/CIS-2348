# Oscar Jasso
# PSID : 1895743

# Finish reading other items into variables, then output the three ingredients
lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings= float(input('How many servings does this make?\n\n'))

print('Lemonade ingredients - yields',f'{servings:.2f}', 'servings')
print(f'{lemon_juice_cups:.2f} cup(s) lemon juice')
print(f'{water_cups:.2f} cup(s) water')
print(f'{agave_nectar_cups:.2f} cup(s) agave nectar\n')

# Prompt user for desired number of servings. Convert and output the ingredients
juice_per_serving = lemon_juice_cups / servings
water_per_serving= water_cups / servings
nectar_per_serving = agave_nectar_cups / servings


serving_ask =  float(input('How many servings would you like to make?\n\n'))

desired_juice= juice_per_serving * serving_ask
desired_water = water_per_serving * serving_ask
desired_nectar = nectar_per_serving * serving_ask

print('Lemonade ingredients - yields',f'{serving_ask:.2f}', 'servings')
print(f'{desired_juice:.2f} cup(s) lemon juice')
print(f'{desired_water:.2f} cup(s) water')
print(f'{desired_nectar:.2f} cup(s) agave nectar\n')


# Convert and output the ingredients from (2) to gallons
juice_gallons= desired_juice/ 16
water_gallons=desired_water/ 16
nectar_gallons=desired_nectar/ 16

print('Lemonade ingredients - yields',f'{serving_ask:.2f}', 'servings')
print(f'{juice_gallons:.2f} gallon(s) lemon juice')
print(f'{water_gallons:.2f} gallon(s) water')
print(f'{nectar_gallons:.2f} gallon(s) agave nectar')
