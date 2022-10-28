# # WHILE LOOPS
#
# counter = 0
#
# while (counter < 10):
#     print("Counter value: " + str(counter))
#     counter += 1
#
#
# # if we want to count all the way to 10
#
# counter = 0
#
# while (counter <= 10):
#     print("Counter value: " + str(counter))
#     counter += 1
#
# # if we want to count down
#
# counter = 10000
#
# while (counter >= 0):
#     print("Counter value: " + str(counter))
#     counter -= 1
#
# # a while loop that never ends
#
# # counter = 0
# #
# # # while (counter < 10):
# # #     print("Counter value: " + str(counter))
# # #
#
# # Multi conditional loops
#
# counter_1 = 0
# counter_2 = 0
#
# while counter_1 <= 10 or counter_2 <= 20:
#     counter_1 += 1
#     print("Counter 1 value: " + str(counter_1))
#
#     if counter_1 > 10:
#         counter_2 += 2
#
#     print("Counter 2 value: " + str(counter_2))
#
# ## variable condition while loop
#
# x_input = int(input("Give a value for x: "))
# counter = 0
# while counter <= x_input:
#     print(str(counter) + " out of " + str(x_input))
#     counter +=1
#


#
#
# # menu select
#
# menu_select = 0
#
# while (menu_select == 0):
#     print("1) Play Game")
#     print("2) Options")
#     menu_select = int(input("Pick a menu option: "))
#
#     if menu_select == 1:
#         print("Entering Game")
#     elif menu_select == 2:
#         print("Entering Options")
#     else:
#         menu_select = 0

# name = "Anne"
#
# for character in name:
#     print(character)
#
# # what happens when you print(name)?
#

letter_input = input("What letter are you looking for? ")
name = "Alex"
for character in name:

    if character == letter_input:
        print("The letter " + letter_input + " can be found in the name " + name)



# for x in range(1,10):
#     print(x)
#
# for x in range(10):
#     print(x)
#
# for x in range(1,10,2):
#     print(x)
#
#
# ## FOR LOOP ASCII ART
#
# for x in range(1,10):
#     print("*" * x)


# for x in range(10,0,-1):
#     print("*" * x)
#
# print(x)
#
# ##NOTE, you must include a step argument when trying to decrement
#
# print(len("Anne"))

# ## name comparison
#
# name_1 = input("Enter name 1:")
# name_2 = input("Enter name 2: ")
# name_1_count = 0
# name_2_count = 0
#
# for y in name_1:
#     name_1_count += 1
#     print("Name 1 letter counter: " + str(name_1_count))
#
# for z in name_2:
#     name_2_count += 1
#     print("Name 2 letter counter: " + str(name_2_count))
#
# if name_1_count > name_2_count:
#     print(name_1 + " has more letters in it than " + name_2)
# elif name_2_count > name_1_count:
#     print(name_2 + " has more letters in it than " + name_1)
# else:
#     print(name_2 + " and " + name_1 + " contain the same amount of letters")
#


# for x in range (10):
#     print("-----X loop count: " + str(x))
#
#     for y in range (10):
#         print("y loop count: " + str(y))
#

