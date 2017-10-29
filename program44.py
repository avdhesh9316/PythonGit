class Calculator():
    def add(self, x, y):
        return x+y
    def sub(self, x, y):
        return x-y
    def mul(self, x, y):
        return x*y
    def div(self, x, y):
        return x/y
    def modulus(self, x, y):
        return x%y
    def floorDiv(self, x, y):
        return x//y
    def __main__(self, x, y):
        print('Addition : {}, Sub : {}, Mult : {}, Division : {}, Modulus : {}, Floor Division : {}' \
        .format(self.add(x,y), self.sub(x,y), self.mul(x,y), self.div(x,y), self.modulus(x,y), self.floorDiv(x,y)))

cal = Calculator()
cal.__main__(10, 3)
