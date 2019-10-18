### MY LIST
guest_names = []
### MY COUNTER
counter = 0
### MY WHILE TRUE
while True:

    print("Enter A to add name to your guset list\nEnter Q to exit the program\n"
          "Enter L to displs the people you inverted already\nEnter C to check if someone is inverted.")




#### TO ADD TO THE LIST
    user = input().upper()

    if user == 'A':

        new_guset = input('Enter the guset name\n').upper()

        guest_names.insert(counter, new_guset)
        counter = counter + 1

####  TO QUIT THE PROGRAM
    elif user == "Q":

        break
## TO GET THE LIST
    elif user == 'L':

        print(guest_names)

## TO CHECK IF YOU NAME IS IN GUEST LIST
    elif user == 'C':
        for guest in guest_names:
            Check = input('what is your name pls\n').upper()
            if Check in guest:
                print('You are inverted')
            else: print('You are not inverted' )

    else: print("ENTER THE CORRECT INPUT PLS\n")
