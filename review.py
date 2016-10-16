#Stack - LIFO

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
		return self.items[len(self.items)-1]
	
	def size(self):
		return len(self.items)
	

#Queue: FIFO

class Queue:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
	
	def enqueue(self,item):
		self.items.insert(0, item)
	
	def dequeue(self):
		return self.items.pop()
	
	def size(self):
		return len(self.items)

#Node class
class Node(object):
	def __init__(self, data=None,next_node=None):
		self.data = data
		self.next_node= next_node
		
	def get_data(self):
		return self.data
	
	def get_next(self):
		return self.next_node
	
	def set_next(self, new_node):
		self.next_node = new_node
		

#Singly Linked List
class SinglyLinkedList(object):
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
			raise ValueError("Data not in list")
		
		return current
	
	def delete(self, data):
		current = self.head
		found = False
		previous = None
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				previous = current
				current = current.get_next()
		
		if current is None:
			raise ValueError("Data not in list")
		
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())


#Sequential Search - Unordered
def seq_search(arr, ele):
	pos = 0
	found = False
	while pos < len(arr) and not found:
		if arr[pos] == ele:
			found = True
		else:
			pos += 1
		
	return found

#Sequential Search - Ordered
def ordered_seq_search(arr, ele):
	pos = 0
	found = False
	stopped = False
	
	while pos < len(arr) and not found and not stopped:
		if arr[pos] == ele:
			found = True
		else:
			if arr[pos] > ele:
				stopped = True
			else:
				pos += 1
		
		return found

#Binary Search: Iteratively
def bin_search(arr, ele):
	first = 0
	last = len(arr) - 1
	found = False
	while first <= last and not found:
		mid = (first+last)/2
		if arr[mid] == ele:
			found = True
		else:
			if arr[mid] > ele:
				last = mid - 1
			else:
				first = mid + 1
	
	return found

#Binary Search: Recursively
def recur_bin_search(arr, ele):
	if len(arr) == 0:
		return False
	else:
		mid = len(arr)/2
		
		if arr[mid] == ele:
			return True
		else:
			if arr[mid] > ele:
				return recur_bin_search(arr[:mid],ele)
			else:
				return recur_bin_search(arr[mid+1:],ele)

#Merge Sort: O(nlogn)
def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr)/2
		left = arr[:mid]
		right = arr[mid:]
		
		merge_sort(left)
		merge_sort(right)
		
		i = 0
		j = 0
		k = 0
		
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i+= 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1
		
		while i < len(left):
			arr[k] = left[i]
			 i += 1
			 k += 1
		
		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1

#Quick Sort: O(nlogn)
def quick_sort(arr):
	quick_sort_help(arr, 0, len(arr)-1)

def quick_sort_help(arr, first, last):
	if first < last:
		splitpoint = partition(arr, first, last)
		
		quick_sort_help(arr, first, splitpoint -1)
		quick_sort_help(arr, splitpoint + 1, last)

def partition(arr, first, last):
	pivotvalue = arr[first]
	leftmark = first + 1
	rightmark = last
	
	done = True
	while not done:
		while leftmark <= rightmark  and arr[leftmark] <= pivotvalue:
			leftmark += 1
		
		while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark -= 1
		
		if rightmark < leftmark:
			done = True
		
		else:
			temp = arr[leftmark]
			arr[leftmark] = arr[rightmark]
			arr[rightmark] = temp
		
		temp = arr[first]
		arr[first] = arr[rightmark]
		arr[rightmark] = temp
		
		return rightmark
		
#Binary Tree - Nodes and List
def BinaryTree(r):
	return [r, [],[]]

def insertLeft(root, newBranch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1, [newBranch,t,[]])
	else:
		root.insert(1, [newBranch,[],[]])
	
	return root

def insertRight(root, newBranch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2, [newBranch,[], t])
	else:
		root.insert(2, [newBranch, [],[]])
	return root
	
def getRootVal(root):
	return root[0]

def setRootVal(root, newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]

#Binary Tree Nodes and References
class BinaryTree(object):
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None
		
	
	def insertLeft(self, newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t
		
	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t
	
	def getRightChild(self):
		return self.rightChild
	
	def getLeftChild(self):
		return self.leftChild
	
	def setRootVal(self, obj):
		self.key = obj
	
	def getRootVal(self):
		return self.key
		
