prompt = "ENTER A NUMBER \n"
number = float(input(prompt))
if number%2 == 0:
    print(number,"IS AN EVEN NUMBER")

elif number%2!= 0:
    print(number,"IS AN ODD NUMBER")
else:
    print("TRY INPUTING A NUMBER")
