class Node(object):
	def __init__(self, value):
		self.value = value
		self.next_node = None
		

def reverse(head):
	current = head
	previous = None
	nextnode = None
	
	while current:
		nextnode = current.next_node
		current.nextnode = previous
		
		previous = current
		current = nextnode
	
	return previous
