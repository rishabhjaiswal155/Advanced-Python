#Important Functions in re module of Python:
''' finditer('RegEx',TargetString) =returns the callable Iterator of matched object
	sub(RegEx,replacement,target String)=returns the modified object after replacement if match found otherwise retuns None
	subn(RegEx,replacement,target String)=retuns the tuple with result String and number of times it replaced
	split('sepeartor',target String)=returns the list
	^a=starts with a
	a$=ends with a
'''

import re
matcher=re.finditer('[0-9]','abd2345@ 456dhjd')
print("Digits found in Target String:")
for m in matcher:
	print("starting index:{},group:{}".format(m.start(),m.group()))

s=re.sub('\\d','#','abcd12fnk45@cj')
print("Replacing Digits with # symbol:",s)

t=re.subn('\\d','#','abcd12fnk45@cj')
print(type(t))
print("result String after replacing digits with #:",t[0])
print("The number of replacement:",t[1])

l=re.split('-','10-20-30-40-50-60')
print("List after split Operation:",l)

s="Learning Python is very easy"
m=re.search('^Learn',s)
if m!=None:
	print("Target String starts with Learn")
else:
	print("Target String does not starts with Learn")
	
s="Learning Python is very easy"
m=re.search('EASY$',s,re.IGNORECASE)
if m!=None:
	print("Target String ends with easy")
else:
	print("Target String does not ends with easy")


	