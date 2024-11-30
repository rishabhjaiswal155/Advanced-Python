#Exception Handling using try and except

try:
	print(10/0)
except ZeroDivisionError:
	print("Denominator should not be Zero")
    
#Exception Handling using try with multiple except block
#Here if exception raised in try block then it search for matching except block from top to down manner
try:
    x=int(input("Enter value of x:"))
    y=int(input("Enter value of y:"))
    print("The Division is:",x/y)
except ArithmeticError:
    print("ArithmeticError:The Denominator value should not be zero")
except ValueError:
    print("ValueError: The value must be integral value")
except ZeroDivisionError:
    print("ZeroDivisionError: The Denominator value should not be zero")
