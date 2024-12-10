#Operator Overloading

class Book:
    def __init__(self,pages):
        self.pages=pages
        
    def __add__(self,other):
        return self.pages+other.pages
    
    def __sub__(self,other):
        return self.pages-other.pages
    
    def __mul__(self,other):
        return self.pages*other.pages
    
    def __truediv__(self,other):
        return self.pages/other.pages
    
    def __floordiv__(self,other):
        return self.pages//other.pages
    
    def __mod__(self,other):
        return self.pages%other.pages
    
    def __pow__(self,other):
        return self.pages**other.pages

b1=Book(300)
b2=Book(10)
print("Addition:",b1+b2)
print("Substraction:",b1-b2)
print("Multiplication:",b1*b2)
print("Division:",b1/b2)
print("Floor Division:",b1//b2)
print("Modulo operation:",b1%b2)
print("Power Operation:",b1**b2)
