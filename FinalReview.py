# # ## EXAM REVIEW
# #
# # ## NOTES: Partial marks will be given for pseudocode or flowchart answers!
# # ## Make sure you understand the symbols for ranges discuess -> [] = inclusive, () = exclusive
# # ## You only have to validate input data if a question does not state you can make assumptions
# #
# # #SECTION 1: Multiple choice (5 questions, 2 marks each)
# # # A program will be given for analysis, multiple choice questions will be based
# # # on analyzing the program
# #
# # #SECTION 2: Problem Solving (1 question, 5 marks)
# # # Logic puzzle, will be 3x3, use logic puzzle site linked in our Logic lecture
# # # to practice
# #
# # #SECTION 3: Conditional Statements/Boolean Logic (2 questions, 5 + 10 marks)
# #
# #Q1
# # #Receive user input that then assess it for specific conditions
# # #Could include conditional logic that requires string slicing and/or string manipulation
# # #Could include conditional logic that requires assessing if an input is within range
# #
# # #Example: Accept some user input and convert it to lower case, then print the input
# # #only if it begins with the letter h.
# #
# user_input = input("Give me some input: ").lower()
#
# if user_input[0] == "h":
#     print(user_input)
#
# #Q2
# #Receive multiple pieces of user input and assess if it matches a mathematical theory
# #Look at the triangle question from Assignment 3 to practice
#
# #Example: Accept two user inputs, one will represent the lenght and the other will represent the
# # width of a 4 sided shape. Determine wheather this shape will be a square or rectangle where
# # a square will fufill the criteria, l = w
# #Validate that the input are integers
#
# length = input("Please enter the length of the shape: ")
# width = input("Please enter the width of the shape: ")
#
# if length.isdecimal() and width.isdecimal():
#     if length == width:
#         print("This shape will be a square")
#     else:
#         print("This shape will be a rectangle")
# else:
#     print("Invalid input")
#
# #Section 4: Repetition Problems (2 questions, 5 + 10 marks)
#
# #Q1
# #Loop over a range of numbers based on user input
# # Use this range of number to perform some calculations in the loop
#
# #Example: Receive user input that is assumed to be an integer > 1.
# # sum all odd numbers between 1 and the user input (including the user input)
#
# user_input = int(input("Enter an integer > 1: "))
# sum = 0
# for x in range(1,user_input + 1):
#     if x % 2 != 0:
#         sum += x
#
# #Q2
#Draw a shape using a loop

#Example: Receive user input that will determine the height of a right
#angle triangle. Create a loop that will draw the triangle using # as the symbol
#Assume user inputs a valid integer
#
# triangle_input = int(input("Please enter the height of the triangle"))
#
# for x in range(1,triangle_input +1):
#     print("#"*x)

#Section 5: List, Data Validation, Function Problems (2 questions, 5 + 10 marks)

#Q1
#Search for specific characters in a string list

#Example: Given a string list, determine how many times the letter p appears

# words = ["hello","people","poet"]
# letterCount = 0
# for x in words:
#     for y in x:
#         if y == "p":
#             letterCount += 1
#
# print(letterCount)
#
# #Q2
#Write a function that checks if a # is prime!

#Section 6: Full program problems (Either 1 or 2 questions, Either 20 marks or 10 + 10 marks)

#This section will ask you to write a longer 'full' program to perform some operation
#May include, user input with data validation
# Creating a list from user input
# Performing string manipultion of user input
# Creating a user menu with options
# Using functions may be helpful for these problems but will not be required

#Example: Ask the user for some input between (10,15)
# Ask the user if they would like do half their input (you can use 'yes', 'no')
# Create a list of numbers between 1 and 100 (inclusive) that are multiples of the input
# EX an input of 12 would result in [ 12,24,48,60,72,84,96]
#Be sure to validate user input

user_input = input("Enter a number between (10,15)")
my_list = []
if user_input.isdecimal():
    user_input = int(user_input)
    if user_input > 10 and user_input < 15:
        while True:
            question = input("Would you like to divide your input by 2? yes,no")
            if question == 'yes' or question == 'no':
                break
            else:
                print("invalid input")

        if question == 'yes':
            user_input = user_input // 2

        for x in range(1,101):
            if x % user_input == 0:
                my_list.append(x)

print(my_list)





