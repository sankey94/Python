with open('fileshalini.txt','r')as h:
	contents=h.read()
	count=0
	word_count={}
	l=contents.split()
	for i in l:
		word_count[i]=word_count.get(i,0)+1
	# 	if i not in word_count:
	# 		word_count[i]=1
	# 	else:
	# 		word_count[i] += 1
	print(word_count)
k=len(l)
print(k)
