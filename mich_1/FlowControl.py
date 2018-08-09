# Michaelmas Lesson 1: Hello World
#
# The second part of this lesson goes into flow control
#
# For license see LICENSE

# take some input
input_number = input("What is your favourite number: ")

# this is the structure of an if statement in Python
#  they're executed top to bottom
#  starting with the first if, then all the elifs
#  and if none were met the else is executed
if int(input_number) == 17:
    print("That's my favourite number")
elif int(input_number) == 13:
    print("I thought that was an unlucky number")
else:
    print("An interesting choice...")

# let's edit it slightly
guessed_right = False
while not guessed_right:
    input_number = input("Guess my favourite number: ")
    if int(input_number) == 17:
        print("That's my favourite number")
        guessed_right = True
    elif int(input_number) == 13:
        print("I thought that was an unlucky number")
    else:
        print("An interesting choice... But not correct!")

# we're going to use the for loop to check if each number between 0 and 100
#  can be divided by some number that the user inputs
divide_number = int(input("Which number shall we check for? "))
for num in range(101):
    remainder = num % divide_number
    if remainder == 0:
        print(str(num) + " can be divided by " + str(divide_number))
    else:
        print(str(num) + " can't be divided by " + str(divide_number))
