from sys import stdout

l1 = [4, 5, 1, 6, 78, 8, 11]
l2 = [9, 15, 53, 82, 7, 8, 14, 20]
l3 = [10, 12, 16, 18, 56, 14, 0]

minlist = []
maxlist = []

def fun1(x):
    min1 = max1 = min2 = max2 = 0
    for i in range(len(x)):
        if x[i] <= x[min1]:
            min1 = i
        if x[i] >= x[max1]:
            max1 = i
    for i in range(1, len(x)):
        if(x[i] != x[min1] and x[i] != x[max1]):
            if x[i] <= x[min2]:
                min2 = i
            if x[i] >= x[max2]:
                max2 = i

    print('min1 : {} max1 : {} min2 : {} max2 : {}'.format(x[min1], x[max1], x[min2], x[max2]))

    minlist.append(x[min1])
    maxlist.append(x[max1])
    minlist.append(x[min2])
    maxlist.append(x[max2])

fun1(l1)
fun1(l2)
fun1(l3)

def average(x):
    sum = 0
    for i in x:
        sum += i
    return sum/len(x)

minListAvg = average(minlist)
maxListAvg = average(maxlist)

for i in [minlist, maxlist]:
    if i == minlist:
        print('minlist : ')
        for j in i:
            stdout.write(' {}'.format(j))
    else:
        print('\nmaxlist : ')
        for j in i:
            stdout.write(' {}'.format(j))

print('\nMinimum List Average : {} and Maximum List Average : {}'.format(minListAvg, maxListAvg))
