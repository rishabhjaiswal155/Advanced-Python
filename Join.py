#join() and join(time in sec) in Thread class which holds to the Main Thread to Complete it execution before completing execution of the calling Thread.

from threading import *
import time
def venue():
    time.sleep(3)
    print("Venue Fixed....")
    
def print_card():
    for t in range(10):
        print("Wedding Card Printing....")
        time.sleep(1)

def distribute_cards():
    for t in range(10):
        print("Distributing Wedding Cards....")
        time.sleep(1)
        
t1=Thread(target=venue)
t2=Thread(target=print_card)
t3=Thread(target=distribute_cards)
t1.start()
#t1.join()
t1.join(3)
print("Wedding Cards Printing stared....")
t2.start()
#t2.join()
t2.join(10)
print("Wedding Cards Printing Done...")
print("Distribution of Wedding Cards Started...")
t3.start()
#t3.join()
t3.join(10)
print("Distribution of Wedding Cards Done....")
time.sleep(3)
print("Marriage preparations Done....")
