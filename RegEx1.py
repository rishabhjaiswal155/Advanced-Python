#Example using REGEX:
''' write a python program to validate identifiers of some language:
The rules for identifiers are:
1.The allowed Characters are alphabets,digits,#
2.The First Character should be lowercase alphabet from a-k
3.The second character should be any digit divisible by 3
4.The Length of Identifier should be atleast 2.'''

import re
s=input("Enter some identifier to validate:")
m=re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',s)
if m!=None:
	print(s,"is valid Identifier.")
else:
	print(s,"is not valid Identifier.")
