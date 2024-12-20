#shallow copy:
'''If the Original object contains any reference to the mutable objects,just
duplicate reference variables will be created pointing to old contained object,
but not duplicate object creation.'''
'''Also if the Original Object does not contain any nested list then
it is same as deepcopy.'''
import copy
l1=[10,20,[30,40],50] #Here original Object conatains reference to another list
l2=copy.copy(l1) #Here only reference variable for nested list is copied,and not the whole object
print(id(l1))
print(id(l2))
l1[0]=15 #Modification in l1
l1[2][1]=888 #Modification in shared nested Object,so it reflects on both l1 and l2
print("l1:",l1) #[15,20,[30,888],50]
print("l2:",l2) #[10,20,[30,888],50]