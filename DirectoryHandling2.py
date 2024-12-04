#os.walk(path,topdown=True,onerror=None,followlinks=False)

import os
for dirpath,dirnames,filenames in os.walk('H:/Advanced Python'):
	print("Current Directory is:",dirpath)
	print("Directory names present in current directory:",dirnames)
	print("File present in the current directory:",filenames)
print("Task Completes...")
