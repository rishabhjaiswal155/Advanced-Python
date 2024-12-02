#Program to take filename as input from keyboard and count the number of lines,characters,words present in the file

import os
fname=input("Enter filename:")
if os.path.isfile:
	print("File Exist:",fname)
	with open(fname,'r') as f:
		lcount=wcount=ccount=0
		for line in f:
			lcount=lcount+1
			ccount=ccount+len(line)
			word=line.split()
			wcount=wcount+len(word)
		print("The number of lines in file:",lcount)
		print("The number of words in file:",wcount)
		print("The number of characters in file:",ccount)
else:
	print("File not Exist:",fname)
			
