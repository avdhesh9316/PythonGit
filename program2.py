class BiggestOfThreeNumber():

	def botn(self, a, b, c):
		if a > b and a > c:
			return a
		elif b > a and b > c:
			return b
		else:
			return c
			
	def __main__(self, x, y, z):
		self.b = self.botn(x, y, z)
		print("The Biggest bumber is {}".format(self.b))
		

big = BiggestOfThreeNumber()	
big.__main__(10, 50, 3)		