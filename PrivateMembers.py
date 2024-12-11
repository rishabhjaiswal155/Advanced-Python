#Private Members:
class Test:
	__x=10
	def __init__(self):
		self.__y=20

t=Test()
#print(t.__x) #These gives error as private members cannot be accessed from outside of class.
#print(t.__y) #These gives error as private members cannot be accessed from outside of class.


print(t.__dict__) #Here Private Members can be accessed outside the class using __dict__ 
print(Test.__dict__)

print(t._Test__x) #Here Private Members can be accessed outside the class using _className__variableName
print(t._Test__y)

#Thus In Python,private Members can be accessed outside of Class technically.