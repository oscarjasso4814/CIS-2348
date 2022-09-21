# Oscar Jasso
# PSID : 1895743

from math import ceil

wall_height = float(input('Enter wall height (feet):\n'))
wall_width = float(input('Enter wall width (feet):''\n'))
wall_area = wall_height * wall_width
print(f"Wall area: {wall_area:.0f} square feet")

paint_gallons = wall_area / 350
print(f"Paint needed: {paint_gallons:.2f} gallons")

gallon_cans_needed = ceil(paint_gallons / 1)
print('Cans needed:', gallon_cans_needed,  'can(s)\n')

color = {'red': 35, 'blue': 25, 'green': 23}
paint_color = input('Choose a color to paint the wall:\n')

cost = color[paint_color]
cost = cost * gallon_cans_needed
print('Cost of purchasing', paint_color, f'paint: ${cost}')
