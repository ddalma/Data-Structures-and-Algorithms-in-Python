
class Queue:
	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return self.items == []
		
	def enqueue(self,item):
		self.items.insert(0,item)
	
	def dequeue(self):
		return self.items.pop()
	
	def size(self):
		return len(self.items)

class Deque:
	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return self.items == []
	
	def addFront(self, item):
		self.items.append(item)
	
	def addRear(self, item):
		self.items.insert(0, item)
	
	def removeFront(self):
		return self.items.pop()
	
	def removeRear(self):
		return self.items.pop(0)
	
	def size(self):
		return len(self.items)



q = Queue()
print q.size()

print q.isEmpty()

q.enqueue(1)
print q.dequeue()


d = Deque()
d.addFront("Hello")
d.addRear("World!")
print d.size()

print d.removeFront() + " "+ d.removeRear()

print d.size()