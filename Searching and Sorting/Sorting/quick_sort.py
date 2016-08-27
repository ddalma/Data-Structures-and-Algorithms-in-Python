def quick_sort(arr):
	quick_sort_help(arr,0, len(arr)-1):

def quick_sort_help(arr, first, last):
	if first < last:
		
		splitpoint = partition(arr, first, last)
		
		quick_sort_help(arr, first, splitpoint - 1)
		quick_sort_help(arr, splitpoint + 1, last)
		
def partition(arr, first, last):
	pivotvalue = arr[first]
	leftmark = first + 1
	rightmark = last
	
	done = False
	while not done:
		while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
			leftmakr = leftmark + 1
			
		while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark = rightmark - 1
		
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
###############################################################

#Stack: LIFO
"""
1. Check if its empty
2. Push items in container
3. Pop items out of container
3. Peek the last item of the container
4. Check the size of the item
"""

class Stack:
	def __init___(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
	
	def push(self, item):
		self.items.append(item)
	
	def pop(self):
		return self.items.pop()
	
	def peek(self):
		return self.items[len(self.items)-1]
	
	def size(self):
		return len(self.items)

#Queue: FIFO
"""
1. Check if its empty
2. Enqueue
3. Dequeue
4. Size
"""

class Queue:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
	
	def enqueue(self, item):
		self.items.insert(0,item)
	
	def dequeue(self):
		self.items.pop()
	
	def size(self):
		return len(self.items)
		

#Node Class:
"""
1. Initialize the data and next node to none
2. getters and setters are getdata, getnext, setnext

"""

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

#Singly Linked-List Class:
"""
1. Initialze the head to none
2. insert
3. size
4. search
5. delete
"""

class SinglyLinkedList(object):
	def __init__(self, head=None):
		self.head = head
	
	def insert(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node
	
	def size(self):
		current = self.head
		count += 0
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
			raise ValueError("Data is not in list")
		
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
			raise ValueError("Data Not in list")
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())

#Sequential Search - unordered
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
	
#Binary Search - Iteratively
def bin_search(arr, ele):
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

#Binary Search - Recursively
def recur_bin_search(arr, ele):
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


#Bubble Sort:
def bubble_sort(arr):
	for i in range(len(arr)-1, 0, -1):
		for k in range(i):
			if arr[k] > arr[k+1]:
				temp = arr[k]
				arr[k] = arr[k+1]
				arr[k+1] = temp

#Selection Sort:
def selection_sort(arr):
	for fillslot in range(len(arr)-1, 0, -1):
		positionMax = 0
			for location in range(1, fillslot+1):
				if arr[location] > arr[positionMax]:
					positionMax = location
			
			temp = arr[fillslot]
			arr[fillslot] = arr[positionMax]
			arr[positionMax] = temp

#Insertion Sort:
def insertion_sort(arr):
	for i in range(1, len(arr)):
		currentvalue = arr[i]
		position = i
		
		while position > 0 and arr[position - 1] > currentvalue:
			arr[position] = arr[position - 1]
			position = position - 1
		
		arr[position] = currentvalue

#Shell Sort:
def shell_sort(arr):
	sublistcount = len(arr)/2
	while sublistcount > 0:
	 for start in range(sublistcount):
	 	gap_insertion_sort(arr, start, sublistcount)
	 
	 sublistcount = sublistcount / 2
	 
def gap_insertion_sort(arr, start, gap):
	for i in range(start + gap, len(arr), gap):
		currentvalue = arr[i]
		position = 1
		
		while position > gap and arr[position - gap] > currentvalue:
			arr[position] = arr[position - gap]
			position = position - gap
		
		arr[position] = currentvalue

def merge_sort(arr):
	if len(arr) == 0:
		return False
	else:
		mid = len(arr)/2
		left = arr[:mid]
		right = arr[mid:]
		
		merge_sort(left)
		merge_sort(right)
		
		i=0
		j=0
		k=0
		
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




