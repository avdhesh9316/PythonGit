
	
class ArithmeticOp():
	def add(self, a, b):
		return a + b;
	
	def subtract(self, a, b):
		return a - b;
		
	def multiply(self, a, b):
		return a * b;
		
	def devide(self, a, b):
		return a / b;
	
	def __main__(self, a, b, c, d):
		print("Addition is : {}".format(a));
		print("Subtraction is : {}".format(b));
		print("Multiplication is : {}".format(c));
		print("Division is : {}".format(d));
		
	
	
obj = ArithmeticOp()
obj.__main__(obj.add(10, 20), obj.subtract(30, 20), obj.multiply(10, 20), obj.devide(50, 20))


		