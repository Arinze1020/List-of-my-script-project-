# IMPORT RANDOM.
import random
# DEFINE MY FIRST FUNCTION FOR STRONGE PASSWORD.
def stronge():
    # CREATED MY RANDOM DIGITE.
    password = "abcdefghijklmnopqrstuvwxyz01234456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # HOM MAY DIGITE THE PASSWORD WELL APPER
    num = 10
    #
    genaretor = "".join(random.sample(password,num))
    return genaretor

first = stronge()
# DEFINE MY SECONDE FUNCTION FOR WEAK PASSWORD.
def weak():
    # CREATED MY RANDOM DIGITE.
    password = "abcdefghijklmnopqrstuvwxyz01234456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # HOM MAY DIGITE THE PASSWORD WELL APPER
    num = 8
    genaretor = "".join(random.sample(password, num))
    return genaretor
second = weak()
# MY MAIN PROGRAM.
while True:

    try:
        print("WELLCOME WE GENARETE  BOTH STRONG AND WEAK PASSWORD CHEAK OUT OUR OPTION.\n OPTION.\n ENTRE A *** FOR STRONG PASSWORD.\n ENTRE B *** FOR WEAK PASSWORD.\n ENTRE Q *** TO QUIT PROGRAM.")

        user_input = input("ENTER YOUR OPTION.\n")

        if user_input == "A":


            print("HERE'S YOUR PASSWORD.\n ==========","\n",first,"\n ==========")


        elif user_input == "B":

            print("HERE'S YOUR PASSWORD.\n ========", "\n", second, "\n ========")

        elif user_input == "Q":

            break


        else:
            print("PLEASE ENTER THE CORRECT OPTION, AND FROM THE OPTION IT SHOULD BE AN UPPERCASE.\n")

    except:

        print("PLEASE ENTER THE CORRECT OPTION,AND FROM THE OPTION IT SHOULD BE AN .\n")

        break

    finally:

        print("THANKS")


