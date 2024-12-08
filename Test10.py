#Instance methods has no decorators
#class methods has @classmethod decorator compulsary
#static method has @static method decorator optional
'''Suppose if one method is define without any decorator,then it may be instance or static method,such method can be identified by its calling,if method is define using object reference variable then it is instance,it its callend by using classname the it is static.'''

class Test10:
    def m1(cls):
        print("Some method: instance or static")

t=Test10()
t.m1() #m1() calling as instance variable
Test10.m1(10) #m1(10) calling as static method.

		