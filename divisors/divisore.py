prompt = "ENTER A NUMBER\n"
user_input = float(input(prompt))

for d in range(0,100):
    if d % user_input == 0:
        print(d)

