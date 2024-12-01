# with statement and keyword 
with open('Rishi.txt','r') as f: #using 'with' keyword,we have not to close the file explicitly using f.close(),it automaticlly close when block execution completes
	data=f.read()
	print("Reading of data completes....")
	print(data)
	print("printing of data completes.....")
	print("is file closed??",f.closed)
print("is file closed??",f.closed)
