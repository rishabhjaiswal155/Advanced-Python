#without using re.compile()

import re #module for Regular Expression
count=0
matcher=re.finditer('ab','abaababa') #finditer() returns the matcher object of given String 
for m in matcher:
	count=count+1
	print("Starting index:{},ending index:{},pattern:{}".format(m.start(),m.end(),m.group()))
print("The Number of occurences:",count)