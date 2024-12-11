#Protected Members:
class Test:
	_x=10
	def __init__(self):
		self._y=20

class Child(Test):
    t=Test()
    print(t._x) #Protected Members can be accessed only in child class or from the class itself
    print(t._y)
		
t=Test()
print(t._x) #But Here Protected Members are also accessed from Outside the class
print(t._y) #So prortected Members is not practically implemented in Python,It only used for symbolic purpose.

c=Child()
