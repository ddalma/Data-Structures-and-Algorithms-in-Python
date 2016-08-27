class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node
		
	def get_data(self):
		return self.data
	
	def get_next(self):
		return self.next_node
	
	def set_next(self, new_next):
		self.next_node = new_next
		

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
		
	def insert(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node
	
	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		
		return count
	
	def search(self, data):
		current = self.head
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()
		
		if current is None:
			raise ValueError("The data is not in the list")
		
		return current
		
	def delete(self, data):
		current = self.head
		previous = None
		found = False
		
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				previous = current
				current = current.get_next()
		
		if current is None:
			raise ValueError("The data is not in the list")
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())



class Stack(object):
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
	
	def push(self, item):
		self.items.append(item)
	
	def pop(self):
		self.items.pop()
	
	def peek(self):
		return self.items[len(items)-1]
	
	def size(self):
		return len(self.items)

		
		