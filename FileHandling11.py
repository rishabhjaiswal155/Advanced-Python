#Running a program,command from python program itself using system() of os module:

import os,datetime
os.system("dir *.py")
os.system("py finallyBlock.py")
os.system("notepad")

#stat() in os module to print statstics of a file

stats=os.stat('Databases.txt')
print(stats)
print("The size of file in bytes:",stats.st_size)
print("The creation time of file is:",stats.st_atime)
print("The creation time of file in timestamp is:",datetime.datetime.fromtimestamp(stats.st_atime))


