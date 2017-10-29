#### Bitwise Operation 

x = int(input()) 
y = int(input())
leftshift = x << y
rightshift = x >> y
band = x & y
bor = x | y 
complement = ~x
exor = x ^ y 

print("{}, {}, {}, {}, {}, {}".format(leftshift, rightshift, band, bor, complement, exor))