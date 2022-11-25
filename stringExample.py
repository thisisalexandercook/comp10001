#Retreive a phrase from the use and format it using the following rules:
# 1) Convert the entire phhrase to lowercase letters
# 2) Upper case every other letters
# 3) Remove any numbers from the phrase, and keep track of the running sum of all numbers removed
# 4) Change any letter e's to 3's, i's to 1's and o's to 0's 

phrase = input("Please enter a phrase")

phrase = phrase.lower()
print(phrase)

count = 0

while count < len(phrase):
    upperCasedLast = True    
    if phrase[count].isalpha():
        if upperCasedLast:
            upperCasedLast = False
        else:
            upperCasedLast = True
            phrase[count]=phrase[count].upper()

    count += 1
    print(count)

print(phrase)

