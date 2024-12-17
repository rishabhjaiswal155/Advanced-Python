#FIFO QUEUE:
import queue
q=queue.Queue()
q.put(10)
q.put(5)
q.put(48)
q.put(49)
q.put(98)
q.put(2)
print("The elements in FIFO QUEUE:",end=" ")
while not q.empty():
	print(q.get(),end=" ")
	
