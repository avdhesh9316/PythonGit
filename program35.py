from sys import stdout

weeks = ('Sun', 'Mon', 'Tue', 'Wed', 'Fri', 'Sat', 'Sun')
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
w_m = weeks + months

for i in range(len(w_m)):
    stdout.write(' {}'.format(w_m[i]))

t1 = (1, 25, 6)
t2 = (7, 10, 20)
t3 = (42, 12, 0)

def findMax(x, y):
    for i in range(len(y)):
        if y[i] >= y[x]:
            x = i
    return y[x]

max1 = max2 = max3 = 0
max1 = findMax(max1, t1)
max2 = findMax(max2, t2)
max3 = findMax(max3, t3)

if max1 > max2 and max1 > max3:
    print('\nTuple 1 is the largest')
elif max2 > max1 and max2 > max3:
    print('\nTuple 2 is the largest')
else:
    print('\nTuple 3 is the largest')


try:
    t1[0] = 4
except TypeError:
    print('Tuple is immutable object. You can not assign item on any index')

t1 = list(t1)
t1.append(100)
print('Inserted Item after typcasting into list {}'.format(t1[t1.__len__() - 1]))
