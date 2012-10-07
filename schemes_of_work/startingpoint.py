# program written by Sue Sentance

import time

def main():
    print("You are trying to find your way through a maze to the centre where ")
    print("there is a pot of gold!")
    print("What you don't know is that this is a dangerous maze with traps and hazards.")
    print()
    print("Starting maze game ...")
    print()
    print("You enter the maze...")
    time.sleep(2) # time.sleep is just used to build up the suspense!
    print("You reach a opening in the wall and go through it...")
    print()
    time.sleep(2)
    print("You can go left (L) or right (R)")
    answer = input("Make your choice ... ")
    print("You chose",answer,"... what will happen? ...")
    time.sleep(2)
    print("You turn the corner...")
    time.sleep(2)
    print("You walk forward a few steps...")
    time.sleep(2)
    if answer == "R":
        print("...and fall down a trap door and are never seen again....")
    else:
        print("...and see a beautiful grassy path lined with trees with a pot of gold at the end!")

    # end of program
