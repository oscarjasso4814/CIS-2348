# Oscar Jasso
# PSID: 1895743

# create exact change function
# take user input and subtract the maximum of each coin from largest value down to lest
# set variable with maximum number of coins for each
def exact_change(user_total):

    dollars = user_total // 100
    dollar_total = dollars * 100

    quarters = (user_total - dollar_total) // 25
    quarter_total = quarters * 25

    dimes = (user_total - (dollar_total + quarter_total)) // 10
    dime_total = dimes * 10

    nickels = (user_total - (dollar_total + quarter_total + dime_total)) // 5
    nickel_total = nickels * 5

    pennies = (user_total - (dollar_total + quarter_total + dime_total + nickel_total))

    return dollars, quarters, dimes, nickels, pennies

# make it so that proper singular and plural amounts are referred to as such


if __name__ == '__main__':

    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if num_dollars > 1:
        print(f'{num_dollars} dollars')
    elif num_dollars == 1:
        print(f'{num_dollars} dollar')

    if num_quarters > 1:
        print(f'{num_quarters} quarters')
    elif num_quarters == 1:
        print(f'{num_quarters} quarter')

    if num_dimes > 1:
        print(f'{num_dimes} dimes')
    elif num_dimes == 1:
        print(f'{num_dimes} dime')

    if num_nickels > 1:
        print(f'{num_nickels} nickels')
    elif num_nickels == 1:
        print(f'{num_nickels} nickel')

    if num_pennies > 1:
        print(f'{num_pennies} pennies')
    elif num_pennies == 1:
        print(f'{num_pennies} penny')

    if input_val <= 0:
        print("no change")
