####  Program 37 Dictonaries

d1 = {'Name': 'Avdhesh', 'Age': 25}
d2 = {'EmpId': 1234, 'Salary': 5000}
d = {**d1, **d2}  ###Merging two dictonaries
d['Salary'] = d['Salary'] + d['Salary']*0.1  ###Updating salary by 10%
#print(d)
d['Age'] = 26
#print(d)
d.__setitem__('Grade', "B1")  ###Adding another item in dictonaries
for i in d.keys():   ### Printing all keys of dictonary
	print(i)
	
for i in d.values():   ### Printing all values of dictonary
	print(i)
	
dic.__delitem__('Age')   ####Deleting an element from list

