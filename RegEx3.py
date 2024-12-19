#Regular Expression Example:
#Enter some mobile number to validate:
#Rules are:
#Mobile number must start with either 6,7,8,9 and must have 10 digits.
#If it have 11 digits then it must start with 0,then either 6,7,8,9 and then any digts upto 9 length 
#If it have 12 digits then it must start with 91,then either 6,7,8,9 and then any digits upto length of 9
#If it have 13 digits then it must start with +91,then either 6,7,8,9 and then any digits upto length of 9

import re
s=input("Enter mobile Number to validate:")
if len(s)==10:
	m=re.fullmatch('[6789]\\d{9}',s)
	if m!=None:
		print(s,"is 10 digit valid Mobile Number.")
	else:
		print(s,"is 10 digit not valid Mobile Number.")
elif len(s)==11:
	m=re.fullmatch('0[6789]\\d{9}',s)
	if m!=None:
		print(s,"is 11 digit valid Mobile Number.")
	else:
		print(s,"is 11 digit not valid Mobile Number.")
elif len(s)==12:
	m=re.fullmatch('91[6789]\\d{9}',s)
	if m!=None:
		print(s,"is 12 digit valid Mobile Number.")
	else:
		print(s,"is 12 digit not valid Mobile Number.")
elif len(s)==13:
	m=re.fullmatch('[+]91[6789]\\d{9}',s)
	if m!=None:
		print(s,"is 13 digit valid Mobile Number.")
	else:
		print(s,"is 13 digit not valid Mobile Number.")
else:
	print(s,"is not either 10,11,12,13 digit valid Mobile Number.")