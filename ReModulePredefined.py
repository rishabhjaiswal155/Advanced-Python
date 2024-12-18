#predefined Character classes:
#\s=space character
#\S=except space character
#\d=any digit
#\D=except digit
#\w=any word character like alphanumeric
#\W=except any word Character
#.=every charcter '''

import re
matcher=re.finditer('.','a789@3 #457sksjh')
for m in matcher:
	print("starting index:{} and pattern:{}".format(m.start(),m.group()))
