#Priority QUEUE: put() contain tuple containing priority number.
import queue
q=queue.PriorityQueue()
q.put((5,"Rishabh"))
q.put((1,"Amol"))
q.put((3,"Shreyash"))
q.put((2,"Guddie"))
q.put((4,"Surabhi"))
q.put((6,"Lucky"))
print("The elements in Priority QUEUE:",end=" ")
while not q.empty():
	print(q.get()[1],end=" ")
	
