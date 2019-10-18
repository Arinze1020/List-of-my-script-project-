i = 1
fac = int(input("enter a num\n"))

if fac == 0 :
    print("THE FACTORIAL OF 0 IS 1")
else :
    for f in range(1,fac+1):
        i = i * f
    print("THE FACORIAL OF",fac,"is",i,"!")