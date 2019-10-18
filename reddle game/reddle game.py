import random


while True:
    a = random.randint(1,4)
    """
           if a == 2:
              print("I HAVE HAND BUT CAN'T CLAPP WHAT AM ?")
           elif a == 3:
                print("I AM BLACK BUT HAVE RED ALL OVER WHAT AM I ?")
           elif a == 1:
                 print("I AM SOMETHING THE BEGINNG AND THE ENDING IS THE SAME WHAT AM ?")


"""
    questions = ["I HAVE HAND BUT CAN'T CLAPP WHAT AM I?", "I AM BLACK BUT HAVE RED ALL OVER WHAT AM I ?",
                 "I AM SOMETHING THE BEGINNG AND THE ENDING IS THE SAME WHAT AM ?" ]


    if a == 2:
        print(questions[0])
        user = input("ENTER YOUR ANSWER\n").lower()

        if user == "clock":
                print("your ans is correct")
        else:
            print("your ans is not correct")
    elif a == 3:
        print(questions[1])

        user = str(input("ENTER YOUR ANSWER\n")).lower()
        if user == "heart":
          print("your ans is correct")
        else:
            print("your ans is not correct")


    elif a == 1:
        print(questions[2])

        user = str(input("ENTER YOUR ANSWER\n")).lower()

        if user == "life":
             print(" your ans is correct.")
        else:
             print("your ans is not correct.")

