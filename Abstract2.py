#Abstract Class Example Fruit

from abc import *
class Fruit(ABC): #Abstract class
	@abstractmethod
	def get_taste(self):
		pass
		
class Orange(Fruit):
	def get_taste(self):
		print("Orange is sour in taste....")
	
	def create_juice(self):
		print("Orange Juice Created...")
		
class Mango(Fruit):
	def get_taste(self):
		print("Mango is Sweet in taste....")
	
	def create_pulp(self):
		print("Mango pulp extracted...")
		
class Apple(Fruit):
	def get_taste(self):
		print("Apple is also sweet in taste...")
		
	def create_Jam(self):
		print("Apple Jam created....")
		
o=Orange()
o.get_taste()
o.create_juice()
m=Mango()
m.get_taste()
m.create_pulp()
a=Apple()
a.get_taste()
a.create_Jam()
