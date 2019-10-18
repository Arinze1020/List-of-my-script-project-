
import random
prompt = "ENTER YOUR GUESS\n"

while True:
    try:
        print("YOU GUESS SHOULID BE IN THE RENGE OF 1-9")
        GUESS = int(input(prompt))

        num = random.randint(1,9)

        if GUESS == num:
            print("YOUR GUESS IS ", GUESS , "EXACTIL RIGHT",num)
            print("HOW WONDERFUL IT FILL TO GET IT")
            break
        elif GUESS < num:
            print("YOUR GUESS IS" , GUESS , " TOO LOW ", num)
        elif GUESS > num:
            print("YOUR GUESS IS",GUESS , "TOO HIGH" , num)
        elif GUESS == "quit":
            break



    except :
        print("THANKE'S FOR PLAYING")
        print("YOU ENETERD INVAILID INPUT")
        break
