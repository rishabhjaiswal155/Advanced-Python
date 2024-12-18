#Important Function in re module
''' match() = returns the matched Pattern if the beginning of pattern matched or else None.
	fullmatch()=returns the fullmatch pattern if the complete pattern is matched or else None.
	search()=returns the first occurrence of pattern if found else returns None.
	findall()=returns the list all ocurrences of pattern if found.
'''

import re
m=re.match('abc','abcdefghituyi')
if m!=None:
	print("matched the beginning,starting index:{},end={},pattern={}".format(m.start(),m.end(),m.group()))
else:
	print("Match pattern is not available..")
m=re.fullmatch('abcdefghituyi','abcdefghituyi')
if m!=None:
	print("fullmatched the pattern,starting index:{},end={},pattern={}".format(m.start(),m.end(),m.group()))
else:
	print("FullMatch pattern is not available..")
m=re.search('def','abcdefghituyi')
if m!=None:
	print("searching pattern found,starting index:{},end={},pattern={}".format(m.start(),m.end(),m.group()))
else:
	print("Searched pattern is not available..")
l=re.findall('abc','abcdefgabchituyi')
print("list of all occurrences:",l)
 