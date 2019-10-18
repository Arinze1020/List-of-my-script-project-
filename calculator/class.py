from math import *
while True:
    print("options:" )
    print("Enter add to add")
    print("Enter sub to subtrant")
    print("Enter mul to multiply")
    print("Enter divid for divition")
    print("Enter mod for modular ")
    print("Enter quit ")

    user_input = input()
    if user_input == "quit":
        print("Thanks")
        break
    elif user_input == "add":
        num1 = float(input("enter num1\n"))
        num2 = float(input("enter num2\n"))
        result = num1 + num2
        print("The sum is ",result )
        break
    elif user_input == "sub":
        num1 = float(input("enter num1\n"))
        num2 = float(input("enter num2\n"))
        result = num1 - num2
        print("The sum is ",result )
        break
    elif user_input == "mul":
        num1 = float(input("enter num1\n"))
        num2 = float(input("enter num2\n"))
        result = num1 * num2
        print("The sum is ", result)
        break
    elif user_input == "divid":
        num1 = float(input("enter num1\n"))
        num2 = float(input("enter num2\n"))
        if num2==0:
            print("You cant divider with zero")
        result = num1 / num2
        print("The sum is ", result)
        break





