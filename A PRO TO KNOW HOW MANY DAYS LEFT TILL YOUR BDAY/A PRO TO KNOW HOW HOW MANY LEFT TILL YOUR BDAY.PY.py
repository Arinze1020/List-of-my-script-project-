import  datetime
#accept user input
useinput = input("ENTER YOUR BRITHDAY 'DD/MM/YY'\n")
brithday = datetime.datetime.strptime(useinput,"%d/%m/%Y").date()

today = datetime.date.today()

thedate = brithday - today

print("YOUR BRITHDAY IS COMING UP ON ",thedate,"FROM NOW")
print(thedate.weeks)