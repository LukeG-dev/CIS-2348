# Luke Gilin 1216992
# Zybooks 7.25 CIS 2348 LAB: Exact change - functions
import math
inputval = int(input())


#  find exact change
def exact_change(user_total):
    new_total = 0
    num_dollars = 0
    num_quarters = 0
    num_dimes = 0
    num_nickles = 0
    num_pennies = 0
    if user_total >= 100:
        num_dollars = user_total / 100
        user_total = user_total % 100
    if user_total >= 25:
        num_quarters = user_total / 25
        user_total = user_total % 25
    if user_total >= 10:
        num_dimes = user_total / 10
        user_total = user_total % 10
    if user_total >= 5:
        num_nickles = user_total / 5
        user_total = user_total % 5
    if user_total >= 1:
        num_pennies = user_total

    return num_dollars, num_quarters, num_dimes, num_nickles, num_pennies


numdollars, numquarters, numdimes, numnickles, numpennies = exact_change(inputval)

#  print exact change
numdollars = math.floor(numdollars)
numnickles = math.floor(numnickles)
numquarters = math.floor(numquarters)
numdimes = math.floor(numdimes)

if inputval <= 0:
    print('no change')
else:
    if numdollars == 1:
        print('{dollar:.0f} dollar'.format(dollar=numdollars))
    elif numdollars > 1:
        print('{dollar:.0f} dollars'.format(dollar=numdollars))

    if numquarters == 1:
        print('{quarter:.0f} quarter'.format(quarter=numquarters))
    elif numquarters > 1:
        print('{quarter:.0f} quarters'.format(quarter=numquarters))

    if numnickles == 1:
        print('{nickle:.0f} nickel'.format(nickle=numnickles))
    elif numnickles > 1:
        print('{nickle:.0f} nickels'.format(nickle=numnickles))

    if numdimes == 1:
        print('{dime:.0f} dime'.format(dime=numdimes))
    elif numdimes > 1:
        print('{dime:.0f} dimes'.format(dime=numdimes))

    if numpennies == 1:
        print('{pennie:.0f} penny'.format(pennie=numpennies))
    elif numpennies > 1:
        print('{pennie:.0f} pennies'.format(pennie=numpennies))


