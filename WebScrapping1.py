#Python Program to extract mobile Numbers from redbus site using webscrapping and Regular Expression.
import re,urllib
import urllib.request
u=urllib.request.urlopen('https://www.redbus.in/info/contactus')
text=u.read()
numbers=re.findall('[+]91[0-9]{10}',str(text))
mail=re.findall('[a-z]+@[a-z]+[.][a-z]+',str(text))
print("Finding contact numbers...")
for n in numbers:
	print(n,'\n')
print("Find contact mail id...")
for m in mail:
    print(m,"\n")