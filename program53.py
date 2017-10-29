#######   Applying all 13 function of File Handling
# 1
fh = open('file.txt', 'r+')
# 2
print(fh.read())
# 3
print('Header is at {}'.format(fh.tell()))
# 4
fh.seek(0)
#5
print('Chuck Size of file header is  : {}'.format(fh._CHUNK_SIZE))
# 6
print('A line of file {}'.format(fh.readline()))
# 7
print('All remaining lines of file : {}'.format(fh.readlines()))
# 8
print('Mode of file header is : {}'.format(fh.mode))
# 9
if fh.readable():
    print('File is readable')
# 10
fh.flush()
# 11
print('File number of file header is : {}'.format(fh.fileno()))
# 12
fh.detach()
fh = open('file.txt', 'r+')
# 13
fh.write('HHH')
# 14
fh.close()
