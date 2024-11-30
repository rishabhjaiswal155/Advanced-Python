#finally block in Exception handling
try:
	x=int(input("Enter number1 : "))
	y=int(input("Enter number2 : "))
	print("The Divison of two number is:",x/y)
except ZeroDivisionError as msg:
	print("Exception caused by:",msg)
except ValueError as msg:
	print("Exception caused by:",msg)
finally:
	print("finally Block always executes")
    
#os._exit(0) only one incident where finally block does not executes i.e when PVM shuts down
import os
try:
    print(10/5)
    print("PVM shuts down.....")
    os._exit(0)
except:
    print("Exception handles in default exception block")
finally:
    print("Finally block")