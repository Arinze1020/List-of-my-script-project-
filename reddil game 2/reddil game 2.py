import random


def getQuestion(request):
    questions = ["I HAVE HAND BUT CAN'T CLAPP WHAT AM I?", "I AM BLACK BUT HAVE RED ALL OVER WHAT AM I ?",
                 "I AM SOMETHING THE BEGINNG AND THE ENDING IS THE SAME WHAT AM ?"]

    print(questions[request])
    print("option -- a b c")

def check_answer(num, ans):
    if num == 0 and ans == "clock":
        return True

    elif num == 1 and ans == "heart":
        return True
    elif num == 2 and ans == "life":
        return True
    else:
        return False



while True:
     num = random.randint(0,2)
     getQuestion(num)

     answer = input("ENTER THE CORRECT ANS?\n.")

     status = check_answer(num, answer)
     if status == True:
        print("the ans is correct")
     else:
         print("THE ANS IS WRONG")
         break

print("you have enter the wrong ans thanks\n.")