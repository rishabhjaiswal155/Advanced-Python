#setter and Getter methods
class Student4:
	def setName(self,name): #Setter method for instance variable name
		self.name=name
	
	def getName(self): #Getter method for instance variable name
		return self.name
	
	def setMarks(self,marks): #Setter method for instance variable marks
		self.marks=marks
	
	def getMarks(self): #getter method for instance variable marks
		return self.marks

l=[]
n=int(input("Enter number of Students:"))
for i in range(n):
    s=Student4()
    name=input("Enter name of Student:")
    marks=int(input("Enter marks of student:"))
    s.setName(name) #calling setter method
    s.setMarks(marks) #calling setter method
    l.append(s)
for s in l:
	print("Student name:",s.getName()) #calling getter method
	print("Student marks:",s.getMarks())#calling getter method
    