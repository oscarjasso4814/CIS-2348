# Oscar Jasso
# PSID : 1895743

print(
    "Davy's auto shop services\n"
    "Oil change -- $35\n"
    "Tire rotation -- $19\n"
    "Car wash -- $7\n"
    "Car wax -- $12\n")

services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': "No service"}

first_service = input('Select first service:\n')
second_service = input('Select second service:\n\n')

first_service_cost = services[first_service]
second_service_cost = services[second_service]

if first_service == '-':
    total_cost = second_service_cost
elif second_service == '-':
    total_cost = first_service_cost
elif first_service == '-' and second_service == '-':
    total_cost = 0
else:
    total_cost = first_service_cost + second_service_cost

print("Davy's auto shop invoice\n")

invoce1 = ""
if first_service == '-':
    invoice1 = "Service 1: No service"
else:
    invoice1 = f'Service 1: {first_service}, ${first_service_cost}'

invoce2 = ""
if second_service == '-':
    invoice2 = "Service 2: No service"
else:
    invoice2 = f'Service 2: {second_service}, ${second_service_cost}'

print(invoice1)
print(invoice2)
print("")
print(f'Total: ${total_cost}')