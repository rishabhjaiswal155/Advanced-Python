#Composition(Strong Association) vs Aggregation(weak Association)

class Student:
	collegeName="IACSD" #static variable
	def __init__(self,name):
		self.name=name #instance variable
		
print(Student.collegeName) #we can access static variable without creating Student's object i.e weak association (Aggregation)
s=Student('Rishabh') #we cannot access instanace variable without creating Student's Object i.e Strong association(Composition)
print(s.name)
		