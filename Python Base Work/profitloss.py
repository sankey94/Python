






invested = input()
sell = input()
if sell > invested: 
	print ('Profit is:', int(sell)-int(invested))
elif sell < invested:
	print ('Loss is:', int(invested)-int(sell))
else:
	print ('Break Even')


	



'''
x = 25
y = 35
if x % 2 == 1 and x > 20:
	print('{} is odd number and it is greater than 20'.format(x))

if False:
	print ('This is true condition')
	print ('Second statement in if block')
	print ('This is third condition')
print ('This is true condition') 
'''
