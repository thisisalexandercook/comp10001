###################
# FUNCTION EXAMPLES
###################

# A SIMPLE PRINT FUNCTION

def helloClass():

    print("hello class")

# MAIN ROUTINE


helloClass()


#########################

# ADDING FUNCTION

def add(x,y):

    my_sum = x + y

    return my_sum

# MAIN ROUTINE


print(add(5, 7))


# A LITERAL RETURN STATEMENT

def return_42():
    return 42

# MAIN ROUTINE


print(return_42())


# AN ACCUMULATOR FUNCTION

def counter(count_parameter):

    count_parameter = count_parameter + 1

    return count_parameter

# MAIN ROUTINE


count = 0
print(count)
count = counter(count)
print(count)
count = counter(count)
print(count)


