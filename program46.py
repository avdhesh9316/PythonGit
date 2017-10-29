def biggestOf4(a,b,c,d):
    if a > b and a > c and a > d:
        print('{} is the biggest'.format(a))
    elif b > a and b > c and b > d:
        print('{} is the biggest'.format(b))
    elif c > a and c > b and c > d:
        print('{} is the biggest'.format(c))
    else:
        print('{} is the biggest'.format(d))
biggestOf4(10, 12, 6, 11)
