#Operator Overloading with more than two Object reference and __str__()

class Book:
	def __init__(self,pages):
		self.pages=pages
	
	def __add__(self,other):
		total=self.pages+other.pages
		return Book(total)
		
	def __str__(self):
		return str(self.pages)
		
b1=Book(100)
b2=Book(250)
b3=Book(300)
b4=Book(150)
print(b1+b2+b3+b4)