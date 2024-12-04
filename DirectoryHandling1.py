#Working with Directories

import os
print("The Current Working Directory is:",os.getcwd())
os.mkdir('Rishi')
print("Making new Directory completes..")
os.mkdir('Rishi/Python')
print("Making subdirectories in already present Directory completes..")
os.makedirs('sub1/sub2/sub3/sub4')
print("Making multiple subdirectories completes..")
os.rmdir('Rishi/Python')
print("Removing a empty sub directory completes...")
os.rmdir('Rishi')
print("Removing directory completes...")
os.removedirs('sub1/sub2/sub3/sub4')
print("Removing multiple sub directories completes...")
os.mkdir("Rishabh")
os.rename('Rishabh','Jaiswal')
print("Renaming directory completes...")
print("Lisiting the directories or showing the content in directory:",os.listdir('.'))


