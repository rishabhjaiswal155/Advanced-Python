#Character Classes:
'''[abc]=either a or b or c
   [^abc]=except a and b and c
   [a-z]=any lower case alphabets
   [A-Z]=any Upper case alphabets
   [a-zA-Z]=any alphabets
   [0-9]=any Digit
   [a-zA-Z0-9]=any alphanumeric 
   [^a-zA-Z0-9]=special symbols except alphanumeric'''
import re
matcher=re.finditer('[^a-zA-Z0-9]','aa7b@k97')
for m in matcher:
	print("starting index:{},ending index:{},pattern:{}".format(m.start(),m.end(),m.group()))
	
   