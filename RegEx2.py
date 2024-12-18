#Regular Expression Example:
#Enter some mobile number to validate:
#Rules are:
#Mobile number must start with either 6,7,8,9 and must have 10 digits.

import re
s=input("Enter mobile Number to validate:")
m=re.fullmatch('[6789]\\d{9}',s)
if m!=None:
	print(s,"is valid Mobile Number.")
else:
	print(s,"is not valid Mobile Number.")