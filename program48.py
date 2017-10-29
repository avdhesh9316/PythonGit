class ArithmeticOp():
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y
    def sqrt(self,x):
        return x ** (1/2)
    def listOfSubStrings(self,s,d):
        return s.split(d)
    def __main__(self, x, y):
        print('Addition : {}, Subtraction : {}, Multiplication : {}, Division : {}' \
        .format(self.add(x,y),self.sub(x,y),self.mul(x,y),self.div(x,y)))

arth = ArithmeticOp()
arth.__main__(5,6)
print('Square root of 16 : '.format(arth.sqrt(16)))
s = 'Pack: My: Box: With: Good: Food'
l = arth.listOfSubStrings(s, ':')
print('New List of Substring is {}'.format(l))
