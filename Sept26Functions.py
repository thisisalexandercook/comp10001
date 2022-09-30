import math
##############################
#TEMPERATURE CONVERSION MODULE
##############################

CONVERSION_CONSTANT = 32


def toCelsius(fahrenheit_input):

    celsius = (5/9)*(fahrenheit_input - CONVERSION_CONSTANT)

    return celsius


c = toCelsius(80.6)
print(round(c,1))


def toFahrenheit(celsius_input):

    fahrenheit = 9/5 * celsius_input + 32

    return "The temperature " + str(celsius_input) + "C is equal to " + str(fahrenheit) + "F"


## MAIN ROUTINE

f = toFahrenheit(27)
print(f)

##########################
#RADIANS CONVERSION MODULE
##########################


def toRadians(degree_input):

    radians = degree_input * (math.pi / 180)

    return radians

## MAIN ROUTINE

rads = toRadians(360)
print(rads)

###################
#BOBBYS BANK MODULE
###################


def bankCalc(bank_input, income_input, rent_input, expense_input ):

    bank_balance = bank_input + income_input - rent_input - expense_input

    return bank_balance

def getBank():

    bank = int(input("What is Bobby's current bank balance? "))

    return bank

## MAIN ROUTINE

bank = getBank()
income = int(input("What is Bobby's income this month? "))
rent = int(input("What is Bobby's rent this month? "))
expense = int(input("What are Bobby's expenses this month? "))


monthly_balance = bankCalc(bank, income, rent, expense)
print(monthly_balance)

################
#COUNTER EXAMPLE
################

counter = 1
counter += 1
print(counter)
