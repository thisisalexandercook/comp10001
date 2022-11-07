# def sumThree(x,y,z):
#
#     totalSum = x + y + z
#
#     return totalSum
#
#
# ##MAIN ROUTINE
#
# firstNum = 5
# secondNum = 6
# thirdNum = 7
#
# totalNum = sumThree(firstNum,secondNum,thirdNum)
#
# print(totalNum)

##VARIABLE TRACE

# firstNum = 5
# secondNum = 6
# thirdNum = 7
#
# totalSum = 18
# totalNum = 18

# def formatNumber(number):
#     if number % 2 == 1:
#         formattedNumber = "-" + str( number ) + "-"
#     else:
#         formattedNumber = "/" + str( number ) + "/"
#     return formattedNumber
#
#
# a = 5
# b = 10
# output = ""
# while a < 20:
#     c = a + b
#     b = a
#     a = c
#     output = output + formatNumber(a)
# print( output )


##VARIABLE TRACE

# a = 5, 15, 20
# b = 10, 5, 15
# output = "", "-15-" , "-15-/20/"
# c = 15, 20
# formattedNumber = "-15-", "/20/"


## Write a python function called seconds2minutes that can accept 1 float parameter = a seconds value and return
## and return a value that converts the seconds input into minutes. There are 60 seconds in a minute. i.e seconds / 60 =
# minutes. For example 120 seconds  = 120 / 60 minutes = 2 minutes. Do not worry about cleaning up the output with rounding etc...

##write a main routine that asks the user for a seconds value, and the displays the output of the function call

# def seconds2minutes(seconds):
#
#     minutes = seconds / 60
#
#     return minutes
#
# ##MAIN ROUTINE
#
# user_input = float(input("What value of seconds would you like to convert? "))
#
# minutes = seconds2minutes(user_input)
# print(minutes)

## if x = 12, what is the result of output = x < 2*2
## ANS = FALSE
#FIB question
#
# x = 12
# output = x < 2*2
# print(output)

## if y = 15 what is the result of output = y >= 5*3
## ANS = TRUE

# y = 15
# output = y >= 5*3
# print(output)

## if a = 15 > 14 and b = 16 > 12 ## What is the output of result = a and b?


## A basketball player can make a free throw 100% of the time if they are 5 feet or less from the basket, and 50% of the time
## if they are between 6 and  10 feet from the basket, any distance further than than and the player has a <25% change of making the basket.
## Write conditional logic with IF statments to represent the players chances. You can compare the players current distance use
## a variable called player_distance. You can store the players chances of scoring as a string in the variable players_chance

# player_distance = 4
#
# if player_distance <= 5:
#     player_chance = "100%"
# elif player_distance >= 6 and player_distance <=10:
#     player_chance = "50%"
# else:
#     player_chance = "<25%"
#
# print(player_chance)

## Gerry is an avid fishermen and knows that the best fish at his local lake are caught at least 10 feet out and
## when the water is calm. Create a variables called calm_water, fish_distance to determine if a variable called
## good_fish will be true or not.

# calm_water = True
# fish_distance = 10
#
# if fish_distance >= 10 and calm_water == True:
#     good_fish = True
# else:
#     good_fish = False
#
# print(good_fish)

## A user enters a number that is saved as an integer called user_input. If user_input is negative, multiply it by (-3),
## if it is positive, multiply it by (2), if it is exactly 0, add 12.

# user_input = int(input("Give me an integer: "))
#
# if user_input < 0:
#     user_input = user_input * (-3)
# elif user_input > 0:
#     user_input = user_input * (2)
# else:
#     user_input = user_input + 12

## Write a while loop that uses a variable called counter to count from 0 to 20 (INCLUSIVE!)

counter = 0

while counter <= 20:
    print(counter)
    counter += 1

## Write a for loop that counts from 0 to 50 in 2s. HINT: use the RANGE function

for x in range(0,51,2):
    print(x)