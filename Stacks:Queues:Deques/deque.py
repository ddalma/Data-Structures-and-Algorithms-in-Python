#Implement a Deque

"""
1. Check if its empty
2. Add to both front and rear
3. Remove from front and rear
4. Check the Size
"""

class Deque:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
	
	def addFront(self, item):
		self.items.append(item)
	
	def addRear(self,item):
		self.items.insert(0, item)
	
	def removeFront(self):
		return self.items.pop()
	
	def removeRear(self):
		return self.items.pop(0)
	
	def size(self):
		return len(self.items)
