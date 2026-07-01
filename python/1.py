# Amazon Fulfillment Centre (Array)

belt = [None, None, None, None, None, None, None, None]

def update_slot():
    slot = int(input("Enter slot number (0-7): "))

    if slot >= 0 and slot < 8:
        product = input("Enter product name: ")
        belt[slot] = product
        print("Slot Updated Successfully")
    else:
        print("Invalid Slot")


def check_slot():
    slot = int(input("Enter slot number (0-7): "))

    if slot >= 0 and slot < 8:
        print("Product in Slot", slot, ":", belt[slot])
    else:
        print("Invalid Slot")


def find_product():
    product = input("Enter product name to search: ")

    found = False

    for i in range(8):
        if belt[i] == product:
            print("Product Found at Slot", i)
            found = True
            break

    if found == False:
        print("Product Not Found")


def check_full():
    full = True

    for item in belt:
        if item == None:
            full = False
            break

    if full:
        print("Belt is Full")
    else:
        print("Belt is NOT Full")


def display_belt():
    print("\nCurrent Belt Status")

    for i in range(8):
        print("Slot", i, ":", belt[i])


while True:
    print("\n===== Conveyor Belt Menu =====")
    print("1. Update Slot")
    print("2. Check Slot")
    print("3. Find Product")
    print("4. Check Belt Full")
    print("5. Display Belt")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        update_slot()

    elif choice == 2:
        check_slot()

    elif choice == 3:
        find_product()

    elif choice == 4:
        check_full()

    elif choice == 5:
        display_belt()

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
    ch = int(input("Enter Choice: "))

    if ch == 1:
        i = int(input("Enter Slot Number: "))
        p = input("Enter Product Name: ")
        update_slot(i, p)

    elif ch == 2:
        i = int(input("Enter Slot Number: "))
        check_slot(i)

    elif ch == 3:
        p = input("Enter Product Name: ")
        find_product(p)

    elif ch == 4:
        is_full()

    elif ch == 5:
        print(belt)

    elif ch == 6:
        break


'''
 ✅H1. Amazon Conveyor Belt Simulation (Array)

Problem Statement

An Amazon fulfillment centre has a conveyor belt with exactly 8 slots numbered 0 to 7. Each slot can store one product.

Implement a Python program to perform the following operations:

Update a product in any slot

Check the product stored at a particular slot

Search for a product in the conveyor belt

Check whether the conveyor belt is completely full

Display all slots of the conveyor belt

Data Structure Used: Array (Python List)

'''