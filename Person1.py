#Inner Class Example

class Person1:
    def __init__(self,name,dd,mm,yyyy):
        self.name=name
        self.dob=self.Dob(dd,mm,yyyy)
        
    def display(self):
        print("Hello",self.name)
        self.dob.display()
        
    class Dob:
        def __init__(self,dd,mm,yyyy):
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy
            
        def display(self):
            print("DOB:{}/{}/{}".format(self.dd,self.mm,self.yyyy))
            
p=Person1('Rishabh',22,4,1996)
p.display()