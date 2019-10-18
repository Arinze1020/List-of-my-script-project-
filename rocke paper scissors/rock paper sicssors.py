import sys
promt = "player one chose your weapon \n"

promt1 = "player two chose your weapon \n"

print("rock\n","paper\n","scissors\n")

playerone = input(promt)

playertwo = input(promt1)
while True:
    if playerone == playertwo:
        print("it`s a tie")




    elif playerone == "rock"and playertwo == "paper":
          print("player two won paper beats rock")
    elif playerone == "rock"and playertwo == "scissors":
          print("player one won rock beats scissors")
    elif playerone == "paper" and playertwo == "rock":
          print("player one won paper beats rock")
    elif playerone == "paper" and playertwo == "scissors":
          print("player two won scissors beats paper")
    elif playerone == "scissors" and playertwo == "rock":
          print("player two won,rock beats scissors")
    elif playerone == "scissors" and playertwo == "paper":
         print("player one won,scissors beats paper")

    else:
         print("invalid input\n")

    break
























