#Priority QUEUE: for strings Priority is in Alphabetical manner(i.e A has Higher Priority,compare to Z)
import queue
q=queue.PriorityQueue()
q.put("Rishabh")
q.put("Amol")
q.put("Shreyash")
q.put("Guddie")
q.put("Surabhi")
q.put("Lucky")
print("The elements in Priority QUEUE:",end=" ")
while not q.empty():
	print(q.get(),end=" ")
	
