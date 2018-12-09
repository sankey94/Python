def recur_factorial(i):
   
   if i == 1:
       return i
   else:
       return i*recur_factorial(i-1)


num =int(input("Enter num:"))
for i in range (1,num+1):
    print( i ,   recur_factorial(i))