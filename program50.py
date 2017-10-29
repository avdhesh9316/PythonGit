####    a   ####
fh = open('file.txt', 'r+')
fh.read()
end = fh.tell()
fh.seek(0)
while fh.tell() != end:
    print(fh.read(10))
    print('I am at {} position'.format(fh.tell()))

#########    b    #########
fh.seek(100)
print('Hello')
print('I am at {}'.format(fh.tell()))
#########    c    ##########
fh.seek(0)
for i in range(5):
    fh.readline()
print("Contents 5th line onwards\n".format(fh.read()))
fh.close()
