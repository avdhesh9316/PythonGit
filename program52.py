from sys import stdout
####    Reversing the lines of the file and printing them

fh = open('file.txt', 'r+')
print(fh.read())
print()
eof = fh.tell()
fh.seek(0)
l = []
while fh.tell() != eof:
    l.append(fh.readline())
for i in range(len(l)):
    print(l.pop())


##########  Reversing contents of file
fh.seek(0)
str = fh.read()
for i in range(len(str)):
    stdout.write(str[len(str) - 1 - i])

fh.close()
