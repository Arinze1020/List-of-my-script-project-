a = [ 1,1,2,3,5,8,13,21,34,55,89]

num = int(input("enter a num"))
new = []
for i in a:

    if i < num:
        new.append(i)
        print(new)
