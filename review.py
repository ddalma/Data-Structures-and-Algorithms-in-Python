class Stack: #LIFO
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

class Queue: #FIFO
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
		
	def enqueue(self, item):
		self.items.insert(0, item)
	
	def dequeue(self):
		self.items.pop()
	
	def size(self):
		return len(self.items)

class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node
	
	def get_data(self):
		return self.data
	
	def get_next(self):
		return self.next_node
	
	def set_next(self, new_next):
		self.next_node = new_node

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
			raise ValueError("Data not is List")
		return current
	
	def delete(self, data):
		current = self.head
		previous = None
		found = False
		while current and found is False:
			if current.get_dat() == data:
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
	
	

#Sequential Search -Unordered
def seq_search(arr, ele):
	pos = 0
	found = False
	while pos < len(arr) and not found:
		if arr[pos] == ele:
			found = True
		else:
			pos += 1
	return found

#Sequential Search - ordered
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

#Binary Search - only used for ordered list
def bin_search(arr, ele): #iteratively
	first = 0
	last = len(arr) - 1
	found = False
	while first <= last and not found:
		mid = (first + last)/2
		if arr[mid] == ele:
			found = True
		else:
			if arr[mid] > ele:
				last = mid - 1
			else:
				first = mid + 1
	return found

def recur_bin_search(arr,ele): #recursively
	if len(arr) == 0:
		return False
	else:
		mid = len(arr)/2
		if arr[mid] == ele:
			return True
		else:
			if arr[mid] > ele:
				return recur_bin_search(arr[:mid], ele)
			else:
				return recur_bin_search(arr[mid+1:], ele)

#Bubble Sort
def bubble_sort(arr):
	for i in range(len(arr)-1, 0, -1):
		for k in range(i):
			if arr[k] > arr[k+1]:
				temp = arr[k]
				arr[k] = arr[k+1]
				arr[k+1] = temp

#Selection Sort
def selection_sort(arr):
	for fillslot in range(len(arr)-1, 0, 1):
		positionMax = 0
		
		for location in range(1, fillslot + 1):
			if arr[location] > arr[positionMax]:
				positionMax = location
		
		temp = arr[location]
		arr[location] = arr[positionMax]
		arr[positionMax] = temp 

#Insertion Sort
def insertion_sort(arr):
	for i range(1, len(arr)):
		currentvalue = arr[i]
		position = i
		
		while position > 0 and arr[position - 1] > currentvalue:
			arr[position] = arr[position -1]
			position = position - 1
		
		arr[position] = currentvalue

#Merge Sort
def merge_sort(arr):
	if len(arr) == 0:
		return False
	
	else:
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
				i += 1
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
			
		 
	