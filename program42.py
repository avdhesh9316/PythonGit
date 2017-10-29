from sys import stdout
n = int(input("Enter number to print fibonnaci series : "))
a = 0
b = 1
c = 1
def fib(n,a,b,c):
    if n == 1:
        stdout.write('{}'.format(a))
    elif n == 2:
        stdout.write('{} {}'.format(a,b))
    else:
        stdout.write('{} {} '.format(a,b))
        for i in range(n - 2):
            b = a + b
            a = c
            c = b
            stdout.write('{} '.format(c))
fib(n,a,b,c)
