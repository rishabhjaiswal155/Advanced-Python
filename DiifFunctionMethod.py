#Difference between function and method

def f1(): #This is called as Function i.e Define outside the class
	print("Hii") 
class Students:
	def m1(self): #It is method i.e Define inside the class
		print("Hello")
f1() #function can be called without creating objects
s=Students()
s.m1() #methods is called by using reference variable of object of class

