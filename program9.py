####    Complex numbers 
class BasicArth():
	def addTwoComplex(self, a, b):
		return a+b
	def subTwoComplex(self, a, b):
		return a-b
	def mulTwoComplex(self, a, b):
		return a*b
	def divTwoComplex(self, a, b):
		return a/b
	def __main__(self, a, b):
		print("Sum is {}, Subtraction is {}, Multi is {}, and Divide is {}".format(self.addTwoComplex(a,b),self.subTwoComplex(a,b), self.mulTwoComplex(a,b), self.divTwoComplex(a,b)))
	
op = BasicArth()
com1 = 4+3j
com2 = 3+5j
op.__main__(com1, com2)