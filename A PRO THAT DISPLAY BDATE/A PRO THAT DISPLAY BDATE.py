import  datetime
# user input
useinput = input("enter your brithdate 'DD/MM/YY'\n ")

brithday = datetime.datetime.strptime(useinput,"%d/%m/%Y")

print(brithday)

