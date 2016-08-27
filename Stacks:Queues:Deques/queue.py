#Implement a Queue

"""
1. Check if Queue is Empty
2. Enqueue
3. Dequeue
4. Return the size of the Queue
"""



class Queue:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
		
	def enqueue(self,item):
		self.items.insert(0, item)
	
	def dequeue(self):
		self.items.pop()
	
	def size(self):
		return len(self.items)