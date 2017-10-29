class OddEven():

	def oddEven(self, num):
		if num % 2 != 0:
			return True
		else:
			return False
	
	def __main__(self, num):
		self.b = self.oddEven(num)
		if self.b:
			print("Number is odd")
		else:
			print("Number is even")
			
	
obj = OddEven()
n = obj.__main__(44)
