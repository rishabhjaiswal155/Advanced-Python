#Assertion in Python
#assert statement used for debugging
#two types of assert statements 1.simple version(without message)2. augmented version(with message)
#syntax: assert condition_expression,message
#if condition false then AsserionError
#To disable assert statements for client py -O test.py
def square_it(x):
	return x*x

assert square_it(2)==4,'Here result must be 4 but it is not'
assert square_it(3)==9,'Here result must be 9 but it is not'
assert square_it(4)==16,'Here result must be 16 but it is not'

print(square_it(2))
print(square_it(3))
print(square_it(4))
print(square_it(5))