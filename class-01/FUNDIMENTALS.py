# First Class sep.23.17

#"print" is the name of the function
#The string "hello world" variable
print("what is your name ")
name = input()

# the variable, a variable is used to store a value

print("hello world " + name + "!")

answer = input ('How many states are therein the united states?\n')

#if/else/elif are used to make decisions on what code to run
#they're called control flow statements because they control the flow of the code
#flow control statements are one of the most fundamental elements od computer programing
if answer == "52":
    print("it can be argued you're correct ")
elif answer =="50":
    print ("you're correct")
else:
    print ("use google to answer all the questions in your Life ")

#exercise: while loop

correct_number = "5"
guess_number = input("I'm thinking of A number between 1 and 10. Guess it!\n")

while guess_number != correct_number:
    print ("sorry try again")
    guess_number = input()

print("you did it" )

# "while" can get you in a lot trouble if you don't have a way  to terminate it.
#exmpl.
while("4" == "4"):
    print('Infinite loop!')

#math problem??

x ='3'
y ='4'
z = x + y
print('z is' + z)

# answer = 34
# add = cast them as integer
z = int(x) + int(y)
print ('now z is {}'. format(z))

#last thing = formatting a string
# what not to do

num = 3
print ('nun is' + num )

# wont work bc you can only concatenate a string with other string.
#the format() functions takes care of this for string as well as other data types, like integers
my_string = 'hello {} '. format('world!')
print(my_string)
my_string_two = 'i am {} years old'
print(my_string_two.format(32))

#next step

correct_number = 7
print('im thinking ofa number between 1 and 10. guess it!')
guess_number = int(input())
while guess_number != correct_number:
    if guess_number < correct_number:
        print('too low, try again')
    else:
        print('too high. try again ')
print ('you did it ')

# guessing game

import random
x = random.randint (1, 20 )
print (x)
