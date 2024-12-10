#Duck Typing Philosophy in Python

class Duck:
	def talk(self):
		print("Quack... Quack....")
		
class Dog:
	def bark(self):
		print("Bhow...Bhow....")
		
def f1(obj):
	if hasattr(obj,'talk'):
		obj.talk()
	elif hasattr(obj,'bark'):
		obj.bark()
		
d1=Duck()
f1(d1)
d2=Dog()
f1(d2)