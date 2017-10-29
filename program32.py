#! /usr/bin/python3

from sys import stdout

list1 = [4, 5, 1, 6, 78]
list2 = [9, 15, 53, 82, 7]
list3 = [10, 12, 16, 18]
print('Length of List1 : {}'.format(len(list1)))
print('Length of List2 : {}'.format(len(list2)))
print('Length of List3 : {}'.format(len(list3)))
min1 = max1 = 0
min2 = max2 = 0
min3 = max3 = 0
for i in range(len(list1)):
    if list1[i] <= list1[min1]:
        min1 = i
    if list1[i] >= list1[max1]:
        max1 = i

for i in range(len(list2)):
    if list2[i] <= list2[min2]:
        min2 = i
    if list2[i] >= list2[max2]:
        max2 = i

for i in range(len(list3)):
    if list3[i] <= list3[min3]:
        min3 = i
    if list3[i] >= list3[max3]:
        max3 = i

if list1[min1] < list2[min2] and list1[min1] < list3[min3]:
    print("List 1 is the smallest")
elif list2[min2] < list1[min1] and list2[min2] < list3[min3]:
    print("List 2 is the smallest")
else:
    print("List 3 is the smallest")

if list1[max1] > list2[max2] and list1[max1] > list3[max3]:
    print("List 1 is the biggest")
elif list2[max2] > list1[max1] and list2[max2] > list3[max3]:
    print("List 2 is the biggest")
else:
    print("List 3 is the biggest")

print('{} {} {} {} {} {}'.format(list1[min1],list1[max1],list2[min2],list2[max2],list3[min3],list3[max3]))

#### Deleting first and last Element
list1.pop()
list2.pop()
list3.pop()
list1.remove(list1[0])
list2.remove(list2[0])
list3.remove(list3[0])
print("New List1 : ")
for i in range(len(list1)):
    stdout.write('{} '.format(list1[i]))

print("\nNew List 2 : ")

for i in range(len(list2)):
    stdout.write('{} '.format(list2[i]))

print('\nNew List 3 : ')

for i in range(len(list3)):
    stdout.write('{} '.format(list3[i]))
