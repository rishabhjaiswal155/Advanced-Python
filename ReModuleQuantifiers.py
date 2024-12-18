#Quantifiers:Number of Occerrences for Character
''' a+=atleast one a i.e 1,2...
	a*=Zero or more a
	a?=atmost one a i.e 0,1
	a{m,n}= minimum m a's and maximum n a's
	a{n}=contains exactly n a's
	^a=starts with a
	a$=ends with a '''
	
import re
matcher=re.finditer('a{2,4}','abaacdakpoaaab')
for m in matcher:
	print("starting at:{},ends at:{},pattern:{}".format(m.start(),m.end(),m.group()))
	