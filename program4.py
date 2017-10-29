class NumPrime():
	
	def numPrime(self, num):
		flag = 0
		i = 2
		while i < num:
			if num % i == 0:
				flag = 1
				break
			i += 1
		if flag == 0:
			return True
		else:
			return False
		
	def __main__(self, num):
		self.b = self.numPrime(num)
		if self.b:
			print("Number is prime")
		else:
			print("Number is not prime")
		
obj = NumPrime()
obj.__main__(11);