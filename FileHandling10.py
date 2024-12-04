#UnZipping of Files
from zipfile import *
f1=ZipFile('Rishabh.zip','r',ZIP_STORED)
names=f1.namelist() #namelist() returns the list of files present in Rishabh.zip
for name in names:
	print("Content of file:",name)
	f2=open(name,'r')
	print(f2.read())
	print()
print("unZipping of file completes")