
prompt = "HOW OLD ARE U NOW\n"
prompt1 = "WHAT IS YOU NAME\n"



try:
    name = input(prompt1)

    user_input = int(input(prompt))
    ans = 2014 - user_input + 100
    print(name,"YOU WILL TURN 100 YEARS ON",ans)

except:
    print("YOU KNOW YOUR AGE STRAT WITH NUMBER AND END WITH NUMBER")
    print("AND THERE SHOULD NOT CONTAIN  LETTERS")
    print("YOU CAN TRY AGAIN")

finally:
    print("THANKS")
