def checkName(name):
    valid = 0
    if len(name) >= 2:
        valid = 1
    else:
        valid = -1
    return valid


def mainLoop():
    busy = 0
    while busy == 0:
        busy = 1
        print("Please enter your name below: ")
        first = input("First name: ")
        last = input("Last name: ")

        if checkName(first) == 1 and checkName(last) == 1:
            print("Valid name!")
            break
        elif checkName(first) != 1 and checkName(last) == 1:
            print("Please enter a longer first name.")
        elif checkName(first) == 1 and checkName(last) != 1:
            print("Please enter a longer last name.")
        elif checkName(first) != 1 and checkName(last) != 1:
            print("Please enter both a longer first and last name.")
        print("---------------------------")
        busy = 0

mainLoop()