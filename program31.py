#! /usr/bin/python3
    ## Sorting a list using selection sort
from sys import stdout
l = []
print('Input 5 numbers to sort : ')
for i in range(5):
    l.append(int(input()))

search = int(input("Search Element : "))

print("Number List")

for i in range(5):
    stdout.write('{} '.format(l[i]))

flag = False
for i in range(5):
    if l[i] == search:
        flag = 1
        break

if flag:
    print("\nSuccess")
else:
    print("\nUnsuccessful Search")
