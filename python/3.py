back_stack = []
forward_stack = []
current = "Home"


def visit():
    global current

    place = input("Enter Place: ")

    back_stack.append(current)
    current = place
    forward_stack.clear()

    print("Current Location:", current)


def back():
    global current

    if len(back_stack) == 0:
        print("No Previous Place")
        return

    forward_stack.append(current)
    current = back_stack.pop()

    print("Current Location:", current)


def forward():
    global current

    if len(forward_stack) == 0:
        print("No Forward Place")
        return

    back_stack.append(current)
    current = forward_stack.pop()

    print("Current Location:", current)


def show():
    print("Current Location:", current)


while True:
    print("\n----- Browser Navigation Menu -----")
    show()
    print("1. Visit Place")
    print("2. Go Back")
    print("3. Go Forward")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        visit()

    elif choice == 2:
        back()

    elif choice == 3:
        forward()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")

'''
✅H3. GPS Navigation System (Stack)

Problem Statement

Develop a simple GPS Navigation System similar to Google Maps.

The system should maintain the user's navigation history using Stacks.

Implement the following operations:

Visit a new place

Go Back to the previous place

Go Forward if available

The navigation should work exactly like the Back and Forward buttons of a web browser.

Data Structure Used: Stack

Programming Language

Python 3

Concepts Used

Functions

List

Array

Stack

Circular Queue

Menu Driven Program
'''
