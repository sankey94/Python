

'''closure is a function which rememebers the value in enclosing scope even if they are not in memory'''






def outer():
    x=10
    def inner(y):
        return x+y
    return inner


local_fun=outer()
print(type(local_fun))
print(local_fun(50))
print(local_fun.__closure__)

'''Closure are used as a function factories.. which returns new and specialised functions'''
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x,exp)
        #Python creates a closure refer to  exp obj
    return raise_to_exp

square=raise_to(2)
cube=raise_to(3)
print(square(5),cube(5))
 
        