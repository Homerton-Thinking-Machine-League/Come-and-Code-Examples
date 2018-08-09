# Michaelmas Lesson 1: Hello World
#
# This is an example solution for the exercise for Week 1
#
# For license see LICENSE

# This file is a solution for the exercise for Week 1. Note the "a": there is more than one valid solution as
#  Programming is an art, not a science and there are good and bad ways to do things, pretty and ugly and if your
#  solution does what we asked. It's a correct one.

# get the input
limit_number = int(input("What number do you want to go up to (and including)?:"))

# count up
for number in range(limit_number + 1):
    # is it divisible by 3 and 5 (FizzBuzz)
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    # what about 3 (Fizz)
    elif number % 3 == 0:
        print("Fizz")
    # what about 5 (Buzz)
    elif number % 5 == 0:
        print("Buzz")
    # it's none of them!
    else:
        print(str(number))

# wasn't too bad was it?
