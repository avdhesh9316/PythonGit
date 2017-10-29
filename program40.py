import time
from sys import stdout
###########   a   ############
for i in range(12):
    print(time.ctime())
    time.sleep(5)

###########   b   ############

start = time.clock()

def fun1():
    for i in range(50):
        stdout.write('{} '.format(i))

fun1()
end = time.clock()

print('\nThe CPU time is {}'.format(end - start))
