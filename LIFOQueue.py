#LIFO QUEUE:
import queue
q=queue.LifoQueue()
q.put(10)
q.put(5)
q.put(48)
q.put(49)
q.put(98)
q.put(2)
print("The elements in LIFO QUEUE:",end=" ")
while not q.empty():
	print(q.get(),end=" ")
	
