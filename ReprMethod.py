#str() vs repr()
#we use str(),when we want to convert our object inti its String representation,but we cannot convert the String representation back into Object using str().
#we use repr() for both converting object into String representation and String into Object.

import datetime
today=datetime.datetime.now()
d1=str(today) #Here we convert object into its String representation
print(d1)
#o1=eval(d1) #Here we try to convert String into object,but gives error
#print(type(o1))

d2=repr(today) #Here we convert Object into its String representation
print(d2)
o2=eval(d2) #Here we convert String into object
print(type(o2))