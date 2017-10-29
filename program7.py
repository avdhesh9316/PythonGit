l = ["He", "She", "hn", "ku", 'c', "kk", "hn", "Hello World!", "Jaipur", ('ty', 'tm', "OL")]

#####  printing all elements

j = 0
for i in l:
	if j == l.__len__() - 1:
		for k in i:
			print(k)
	else:
		print(i)
	j += 1
	
	
	
#####  Slicing

print(l[0 : l.__len__() - 1])
print(l[l.__len__() - 1 : l.__len__()])


######  Repetition

j = 0
for i in l:
	if j == l.__len__() - 1:
		for k in i:
			print(k*5)
	else:
		print(i*5)
	j += 1
	
######   concatenation with other list 

l1 = ['dbfw', 'dmwejf', 'wejfbjfb']

l.append(l1)
print(l)

for i in l:
	if j >= l.__len__() - 2:
		for k in i:
			print(k)
	else:
		print(i)
	j += 1


