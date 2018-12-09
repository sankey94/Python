def fibo(a,b,n):
    print(a,b,end=",")
    while(n-2):
        c=a+b
        a=b
        b=c
        print(c,end=",")
        n=n-1
      
a=int(input('enter the no'))
b=int(input('enter the another no'))
n=int(input('enter the no'))
fibo(a,b,n)      
    




