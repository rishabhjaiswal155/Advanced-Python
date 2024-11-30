#printing Exception message using 'as' Keyword
try:
	print(10/0)
except ZeroDivisionError as msg:
	print("Exception ocurred and its cause is:",msg)

#Exception handling using try and single except block that can handle mutiple Exceptions

try:
    x=int(input("Enter value of x:"))
    y=int(input("Enter value of y:"))
    print("The Division is:",x/y)
except (ZeroDivisionError,ValueError,ArithmeticError) as msg:
	print("Exception cause is:",msg)
	
#Default except block (It must be present at last if there are multiple except blocks are present)

try:
    x=int(input("Enter value of x:"))
    y=int(input("Enter value of y:"))
    print("The Division is:",x/y)
except IndexError as msg:
    print("Exception caused by:",msg)
except OverflowError as msg:
    print("Exception caused by:",msg)
except TypeError as msg:
    print("Exception caused by :",msg)
except:
	print("Exception caused by default exception block:")
	