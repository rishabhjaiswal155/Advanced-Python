#Example of Factorial using Recursion with RLock():
from threading import *
l=RLock()
def factorial(n):
    l.acquire()
    result=0
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    l.release()
    return result

def results(n):
    print("The Factorial of",n,"is:",factorial(n))

t1=Thread(target=results,args=(5,),name='Fact5')
t2=Thread(target=results,args=(9,),name='Fact9')
t1.start()
t2.start()
print(t1.name,"is Alive:",t1.is_alive())
print(t2.name,"is Alive:",t2.is_alive())
print("End of Application...")		
