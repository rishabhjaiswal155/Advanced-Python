#Python Program to validate car Registration number of Maharashtra state.
import re
rn=input("Enter Car Registration number without space:")
reg=re.fullmatch('MH\\d{2}[a-zA-Z]{2}\\d{4}',rn,re.IGNORECASE)
if reg!=None:
	print(rn,"is valid Car Registration number of Maharashtra State")
else:
	print(rn,"is not valid Car Registration number of Maharashtra State")