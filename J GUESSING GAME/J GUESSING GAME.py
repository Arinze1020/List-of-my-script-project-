
print ('GUESS A NUMBER BETWEEN 1 to 10\nchoose N for NO and Y for YES\nis your guess  <= 10')



user = input("").upper()
if user == "Y":
    print("your guess might be 10 or is your guess  <= 5")

    user = input("").upper()
    if user == "Y":
        print("your guess might be 5 or is your guess 0 when you divide by 2")

        user = input("").upper()
        if user == "Y":

            print("your guess is 4")

        elif user == "N":
            print("your guess is 2")

    elif user == "N":
        print("your guess might be 5 or is your guess 1 when you multile it with 1")

        user = input("").upper()
        if user =="Y":
            print("your guess is 1")
        elif user =="N":
            print("your guess is 3")
elif user =="N":
    print("your guess might be 5 or is your guess divisble by 2")
    user = input("").upper()
    if user == "Y":
        print("your guess divisble by 4")
        user = input("").upper()
        if user =="Y":
            print("your guess is 8")
        elif user =="N":
            print("your guess is 6")
    elif user == "N":
        print("your guess divisble by 3")
        user = input("").upper()
        if user == "Y":
            print("your guess is 9")
        elif user == "N":
            print("your guess is 7")








