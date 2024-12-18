#Regular Expression using re module
import re #module for Regular Expression
count=0
pattern=re.compile('ab') #compile() returns the RegEx object of given pattern(optional)
matcher=pattern.finditer('abaababa') #finditer() returns the matcher object of given String 
for m in matcher:
	count=count+1
	print("Starting index:{},ending index:{},pattern:{}".format(m.start(),m.end(),m.group()))
print("The Number of occurences:",count)

#start(): returns the starting index of matcher object
#end():return the ending index of matcher object (endindex+1)
#group() returns the matches String
