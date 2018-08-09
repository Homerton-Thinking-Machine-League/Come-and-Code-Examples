# Michaelmas Lesson 1: Hello World
#
# The first part of this lesson teaches some very basics of input and output using Python.
#
# For license see LICENSE

# Welcome! These example files are here to help you if you get stuck.
# DON'T JUST COPY AND PASTE, if you do this it is very unlikely you'll understand
#  what's going on. If you don't *understand* after reading this example file
#  ASK A DEMONSTRATOR. It's better to ask now and grasp the basics than
#  be so stumped later that you give up the course...
#
# Have fun...

# The first thing we can do is to print something to the output.
print("Hello World!")

# But that's not very interesting...
# Let's get the user's name in there too!

# We declare a variable to store stuff in and give it a name "user_name"
# They're called variables because, they, well vary. They can change
# and that's why they're so useful. Think of them like boxes to put
# things to remember in.

# We can then get some input for the user and give them a prompt...
users_name = input("What is your name? ")
print("Hello there " + users_name)

# I wonder if we could do some maths
some_number_input = input("Give me a number: ")
some_number = int(some_number_input)
added_ten = 10 + some_number
# hang on! why did we do int() before we used it
# read the bit on types on the wiki for this lesson for an explanation

# You should know what's going on here now,
added_ten_string = str(added_ten)

# and here...
print("Look I know that " + some_number_input + " + 10 is "+ added_ten_string +"!")

# BASIC MATHEMATICAL OPERATORS
# let's store a number to do our calculations with
big_number = 1200
print('We started with ' + str(big_number))
# we can do basic addition
big_number_add = big_number + 217
print('Adding 217 got us ' + str(big_number_add))
# or subtraction
big_number_take = big_number - 231
print('Taking 231 got us ' + str(big_number_take))
# or multiplication
big_number_multiply = big_number * 42
print('Multiplying by 42 got us ' + str(big_number_multiply))
# or take a number to a power such as 2 cubed
print('2 cubed is ' + str(2**3))

# DIFFERENT TYPES OF DIVISION
# 'float' division
third = 1 / 3
print('1/3 got us ' + str(third))
half = 1.0 / 2.0
print('1.0/2.0 got us ' + str(half))
# integer division
result_one = 64 // 20
print('64//20 gave us ' + str(result_one))
result_two = 30.0//9.0
print('30.0//9.0 gave us ' + str(result_two))

# MODULO OPERATOR
# when it goes in exactly we get 0
print('6 % 3: ' + str(6 % 3))
print('4 % 2: ' + str(4 % 2))
# if not we get the remainder
print('9 % 2: ' + str(9 % 2))
print('562 % 52: ' + str(562 % 52))