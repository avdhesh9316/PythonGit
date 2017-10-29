
########    a    ###########

from sys import argv
for i in argv:
	if i == 'program5.py':
		continue
	print(i + " ")
	
	
########    b    ###########

big = 0
for i in argv:
	if i == 'program5.py':
		continue
	if int(i) >= big:
		big = int(i)
print("Big number is {}".format(big))