#Operator Overloading 

class Student:
	def __init__(self,name,marks):
		self.name=name
		self.marks=marks
	
	def __lt__(self,other):
		return self.marks<other.marks
	def __gt__(self,other):
		return self.marks>other.marks
	def __le__(self,other):
		return self.marks<=other.marks
	def __ge__(self,other):
		return self.marks>=other.marks
	def __ee__(self,other):
		return self.marks==other.marks
	def __ne__(self,other):
		return self.marks!=other.marks
	
	
s1=Student("Rishabh",92)
s2=Student("Vishal",89)
print("s1<s1",s1<s2)
print("s1<=s1",s1<=s2)
print("s1>s1",s1>s2)
print("s1>=s1",s1>=s2)
print("s1==s1",s1==s2)
print("s1!=s1",s1!=s2)