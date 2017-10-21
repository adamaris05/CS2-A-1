#oct 7,2017

import time


# def tell pyton is a function
def display_intro():
    print('game intro from display_intro')
    print()
# and --> poerator that makes twon boolean values
#t and t = t
#f and f = f
#t and t =f

#or --> operator
# t and t = t
#f and t = t
# f and f =t

def choose_cave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave will you enter? (1 or 2) ")
        cave = input()
    return cave # functions output

def check_cave(cave_chosen):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    print()
    time.sleep(2)
    friendly_cave = str(random.randint(1, 2))
    if cave_chosen == friendly_cave:
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")



play_again = "yes"
while play_again == "yes":
    # play game here
    display_intro()
    cave_number = choose_cave()
    # print("Player chose cave number {}".format(cave_number))
    check_cave(cave_number)
    play_again = input("Want to play again? ")
