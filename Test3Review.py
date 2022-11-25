## using a loop, build a string that prints all the even number between 0 and 100 inclusive.
## Remember, in python 0 is even!

output = ""

for x in range(0,101,2):

    output += str(x) + ", "

print(output)

#What if we want to count every odd number?

output = ""

for x in range(1,101,2):

    output += str(x) + ", "

print(output)


## Obtain a positive integer from the user between 1 and 25
## if the input is divisible by 5, double it
## Calculate the sum of all numbers between the user input and 100
## If the sum becomes > 1000 while looping, break the loop and print "sum to large!"

user_input = int(input("Select a number between 1 and 25 (inclusive)"))

if user_input % 5 == 0:
    user_input = user_input *2

sum = 0
for x in range(user_input, 101, 1):
    sum += x

    if sum > 1000:
        print("sum too large!")
        break

print(sum)

## Complete the following tasks on the list years = [1989,2000,1956,1998,1908,1989]
## 1) Remove 1989 from the list
## 2) Add 2022 to the list
## 3) Write code to see if 1989 is still in the list anywhere, if it is, remove it.
## 4) Sort years using the built in function

years = [1989,2000,1956,1998,1908,1989]

years.remove(1989)
print(years)

years.append(2022)
##or
years = years + [2022]
print(years)

for x in years:
    if x == 1989:
        years.remove(1989)

print(years)

years = sorted(years)
print(years)

## Using the list myList = [1,5,6,9,10,6,3,6], write a loop that counts how many times the number 6
## occurs in the list

myList = [1,5,6,9,10,6,3,6]
findCount = 0
for x in myList:
    if x == 6:
        findCount += 1

print("The number 6 occurs " + str(findCount) + " times in the list")

##Create a menu that allows 2 user inputs: 1) A movie title, 2) What they rate it out of 5 (1-5)
##Convert their rating to stars (i.e a rating of 3 would be ***)
## Store the movie title and star rating in a list called movie_stats
## Store each movie_stats list in another List called movieList (i.e a two dimensional list)


menuFlag = 0
movieList = []

while menuFlag == 0:
    movie_input = input("Enter a movie or the word done to exit")
    if movie_input == "done":
        break
    else:
        movie_rating = input("Enter a rating from 1-5 to convert to stars")
        movie_rating = str(int(movie_rating)*"*")
        movie_stats = [movie_input,movie_rating]
        movieList += [movie_stats]

print(movieList)
