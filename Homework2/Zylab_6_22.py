# Oscar Jasso
# PSID: 1895743

# ask for inputs
a = int(input())
b = int(input())
c = int(input())


d = int(input())
e = int(input())
f = int(input())

solution = ""

# attempt all the combinations for x and y between -10 and 10 in given form
# if variables give desired result insert them into the solution variable
for x in range(-10, 10):
    for y in range(-10, 10):
        if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
            solution += f'{x} {y}'

# if variables dont work print out no solution
# if variable found print solution
if solution == "":
    print("No solution")
else:
    print(solution)
