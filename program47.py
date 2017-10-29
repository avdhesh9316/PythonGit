def extendTuple(t,l):
    for i in l:
        t += (i,)
    print('Now New Tuple {}'.format(t))
t = (1,2,3,4,)
l = [5, 6, 7, 8, 9, 10]
extendTuple(t,l)
