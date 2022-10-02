##RELATIONAL EXPRESSIONS
x = 3 > 4
print(x)

y = 3 == 3
print(y)

##BOOLEAN OPERATORS
z =  x and y
print(z)

z =  x or y
print(z)

z = not x and y
print(z)

z =  x ^ y
print(z)
#oxr operator
z = not (x and y)
print(z)
#nand operation

z = not(x or y)
print(z)
#nor operation

##DE MORGANS LAW EXAMPLE
print("De Morgans Law")

a = True
b = False
# 	not ( a and b ) = not (a) or not(b)
demorgan1a = not (a and b)
print(demorgan1a)
demorgan1b = not a or not b
print(demorgan1b)
demorgan1Check = demorgan1a == demorgan1b
print(demorgan1Check)

# 	not ( a or b ) = not (a) and not (b)

demorgan2a = not(a or b)
print(demorgan2a)
demorgan2b = not a and not b
print(demorgan2b)
demorgan2Check = demorgan2a == demorgan2b


### IF STATEMENTS

p = 4
q = 5

if p > q:
    print("We made it")

if q > p:
    print("No! We made it here!")

## IF ELSE STATEMENT

if p > q:
    print("p is greater than q")


else:
    print("q is greater than p")

## note that all conditions are included in an if else statement, so 1 body is
## always going to run

## ELIF STATEMENTS

if p > q:
    print("we're in the if statement")
elif q == p:
    print("we're in the elif statement")
else:
    print("we're in the else statement ")


##HENRYS WORD PROBLEM


FOODCONSTANT = 15


def calcFoodWeight(bodyweight_input, supplement_weight_input):

    food_weight = FOODCONSTANT*bodyweight_input + supplement_weight_input

    return food_weight


def calcSupplementWeight(day_value):

    if day_value % 2 == 0:
        supplement_weight = 10
    else:
        supplement_weight = 5

    return supplement_weight

def getDayValue():

    day_value = int(input("What day of the year is it? "))

    return day_value


def getBodyweight():

    bodyweight = int(input("How much does Henry currently weight? (lbs) "))

    return bodyweight


henrys_weight = getBodyweight()
day_in_year = getDayValue()
supp_weight = calcSupplementWeight(day_in_year)
food_weight = calcFoodWeight(henrys_weight,supp_weight)
print(str(food_weight) + " grams")

