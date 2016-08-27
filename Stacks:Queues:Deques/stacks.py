#Implement a stack

"""
1. Check if its empty
2. Push a new item
3. Pop an item
4. Peek at the top item
5. Return the size
"""



class Stack:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
	
	def push(self, item):
		self.items.append(item)
	
	def pop(self):
		self.items.pop()
	
	def peek(self):
		return self.items[len(self.items) - 1]
	
	def size(self):
		return len(self.items)

s = Stack()

s.push(14)
s.push(13)
s.push(12)
s.push(11)

	
print s.peek()
print s.size()

s.pop()
s.pop()

print s.size()
print s.peek()
