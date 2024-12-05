#Initialize varaible without using constructor
class Person:
	def initialize(self):
		self.name='Rishabh'
		self.age=28
		self.city='Akola'
	def display(self):
		print("Person's Name is:",self.name)
		print("Person's Age is:",self.age)
		print("Person's City is:",self.city)
p=Person()
p.initialize()
p.display()

		