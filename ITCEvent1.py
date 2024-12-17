#Interthread Communication (Trafficpolice and Driver example):
from threading import *
import time
e=Event()
def trafficpolice():
	while True:
		time.sleep(10)
		print("Traffic Police giving GREEN signal...")
		e.set()
		time.sleep(10)
		print("Traffic Police giving RED signal...")
		e.clear()
def driver():
	num=0
	while True:
		print("Drivers waiting for GREEN signal...")
		e.wait()
		print("Traffic Signal is GREEN...Vehicles can move...")
		while e.is_set():
			num=num+1
			print("Vehicle Number:",num,"Crossing the signal..")
			time.sleep(2)
		print("Traffic Signal is RED....Drivers have to wait..")
t1=Thread(target=driver)
t2=Thread(target=trafficpolice)
t1.start()
t2.start()
