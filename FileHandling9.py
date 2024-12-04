#Zipping of files

from zipfile import * #zipfile is module
f=ZipFile('Rishabh.zip','w',ZIP_DEFLATED) #ZipFile is class in zipfile module
f.write('Languages.txt')
f.write('Databases.txt')
f.write('Framework.txt')
print("Zipping of Files completed")

