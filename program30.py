#! /usr/bin/python3
    ## Sorting a list using selection sort
from sys import stdout
l = []
print('Input 5 numbers to sort : ')
for i in range(5):
    l.append(int(input()))

print("Number List without sorting")

for i in range(5):
    stdout.write('{} '.format(l[i]))


for i in range(0,4):
    min1 = i
    for j in range(i+1,5):
        if l[j] <= l[min1]:
            min1 = j
        l[i],l[min1] = l[min1],l[i]

print("\nNumber List with sorting")
for i in range(5):
    stdout.write('{} '.format(l[i]))
