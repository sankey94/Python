def hcfnum0(num1,num2):
    if num1<num2:
        smaller=num1
    else:
        smaller=num2
    for i in range(1,smaller-1):
        if(num1%i==0)and(num2%i==0):
            hcf=i
    return hcf

def hcfnum(num1,num2):
    smaller=min(num1,num2)
    for i in range(1,smaller-1):
        if(num1%i==0)and(num2%i==0):
            hcf=i
    return hcf
            
num1=int(input("Enter first num:"))
num2=int(input("Enter second num:"))

print("HCF of ",num1,"and",num2," is :",hcfnum(num1,num2))
