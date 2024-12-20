#Deep copy:
'''If the Original object contains any reference to the mutable object then
also the whole copy of Object is created.'''

import copy
l1=[10,20,[30,40],50] #Here original Object conatains reference to another list
l2=copy.deepcopy(l1) #Here the whole object is copied.
print(id(l1))
print(id(l2))
l1[0]=15 #Modification in l1
l1[2][1]=888 #Modification in nested Object of l1,so it does not reflects on l2
print("l1:",l1) #[15,20,[30,888],50]
print("l2:",l2) #[10,20,[30,40],50]

#If Original Object does not contain any nested mutable objects then both shallow and deep is same.
#copy() of list object is shallow copy.