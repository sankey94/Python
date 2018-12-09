def factpat(no):
    if no==1:
        return no
    else:
        return no*factpat(no-1)


no=int(input("Enter number:"))
for i in range(1,no+1):
    print(i,   factpat(i))