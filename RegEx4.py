#Python program to validate email id using Regular Expression.
import re
m=input("Enter mailid to validate:")
mail=re.fullmatch('\\w+\\W*@[a-z0-9]+[.]com',m)
if mail!=None:
	print(m,"is valid mailid")
else:
	print(m,"is not valid mailid")