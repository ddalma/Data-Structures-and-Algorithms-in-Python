#Implementing a Stack: LIFO
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

#Implementing a Queue: FIFO
class Queue:
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

#Implementing a Deque
def Deque:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
	
	def addRear(self, item):
		self.items.insert(0, item)
	
	def addFront(self, item):
		self.items.append(item)
	
	def removeFront(self):
		self.items.pop()
	
	def removeRear(self):
		self.items.pop(0)
	
	def size(self):
		return len(self.items)
		

#Simple balanced parenthesis:
def genParChecker(symbolString):
	s = Stack()
	index = 0
	balanced = True
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol == '(':
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()
		
		index += 1
	
	if balanced and s.isEmpty():
		return True
	else:
		return False

#General balanced parenthesis:
def generalParChecker(symbolString):
	s = Stack()
	index = 0
	balanced = True
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol in '({[':
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				top = s.pop()
				if not matched(top, symbol):
					balanced = False
		
		index += 1
	
	if balanced and s.isEmpty():
		return True
	else:
		return False

def matched(open, close):
	opens = '({['
	closes = ')}]'
	return opens.index(open) == closes.index(close)
	

#Decimal to binary converter:
def decToBin(decNumber):
	remstack = Stack()
	while decNumber > 0:
		rem = decNumber %  2
		remstack.push(rem)
		decNumber = decNumber // 2
	
	binString = ""
	while not remstack.isEmpty():
		binString = binString + str(remstack.pop())
	return binString

#Decimal to any Base converter:
def baseConverter(decNumber, base):
	digits = '0123456789ABCDEF'
	remstack = Stack()
	while decNumber > 0:
		rem = decNumber % base
		remstack.push(rem)
		decNumber = decNumber // base
	
	newString = ""
	while not remstack.isEmpty():
		newString = newString + digits[remstack.pop()]
	
	return newString

#Palindrome Checker
def palChecker(aString):
	charDeque = Deque()
	
	for ch in aString:
		charDeque.addRear(ch)
	
	stillEqual = True
	
	while charDeque.size() > 1 and stillEqual:
		first = charDeque.removeFront()
		last = charDeque.removeRear()
		
		if first != last:
			stillEqual = False
	
	return stillEqual

#Linked List: Node Class
class Node:
	def __init__(self, initData):
		self.data = initData
		self.next = None
	
	def getData(self):
		return self.data
		
	def getNext(self):
		return self.next
	
	def setData(self, newdata):
		self.data = newData
	
	def setNext(self, newnext):
		self.next = newnext

class UnorderedList:
	def __init__(self):
		self.head = None
	
	def isEmpty(self):
		return self.head == None
	
	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
	
	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		
		return count
	
	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		
		return found
	
	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

#Anagram checker: 1
def anagram(s1,s2):
	s1 = s1.replace(' ','').lower()
	s2 = s2.replace(' ','').lower()
	
	return sorted(s1) == sorted(s2)

#Anagram checker: 2
def anagram(s1, s2):
	s1 = s1.replace(' ','').lower()
	s2 = s2.replace(' ','').lower()
	
	if len(s1) != len(s2):
		return False
		
	count = {}
	
	for letter in s1:
		if letter in count:
			count[letter] += 1
		else:
			count[letter] = 1
	
	for letter in s2:
		if letter in count:
			count[letter] -= 1
		else:
			count[letter] = 1
	
	for k in count:
		if count[k] != 0:
			return False
	
	return True

#Array Pair Sum
def pair_sum(arr, k):
	
	if len(arr) < 2:
		return
	
	seen = set()
	output = set()
	
	for num in arr:
		target = k - num
		
		if target not in seen:
			seen.add(num)
		else:
			output.add( (min(num, target), max(num,target)))
	
	return len(output)

#Largest Continuous Sum:
def large_cont_sum(arr):
	if len(arr) == 0:
		return 0
	
	current_sum = max_sum = arr[0]
	for num in arr[1:]:
		current_sum = max(current_sum + num, num)
		max_sum = max(current_sum, max_sum)
	
	return max_sum
	


"""
Recursions

"""
#Reverse a String:
def reverse(s):
	if len(s) <= 1:
		return s
	
	else:
		return reverse(s[1:]) + s[0]

#String Permutation
def permute(s):
	out = []
	
	if len(s) == 1:
		out = [s]
	
	else:
		for i, let in enumerate(s):
			for perm in permute(s[1:] + s[i+1:]):
				
				out += [let + perm]
	
	return out







#Stack
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

#Queue
class Queue:
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

#Deque
class Deque:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
	
	def addRear(self, item):
		self.items.insert(0, item)
	
	def addFront(self, item):
		self.items.append(item)
	
	def removeFront(self):
		self.items.pop()
	
	def removeRear(self):
		self.items.pop(0)
	
	def size(self):
		return len(self.items)

def par_checker(symbolString):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol == '(':
			s.push(symbol):
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()
		
		index += 1
	
	if balanced and s.isEmpty():
		return True
	else:
		return False

def gen_par_checker(symbolString):
	index = 0
	s = Stack()
	balanced = True
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol in '({[':
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				top = s.pop()
				if not matched(top, symbol):
					balanced = False
		index += 1
	
	if balanced and s.isEmpty():
		return True
	else:
		return False

def matched(open, close):
	opens = '({['
	closes = ')}]'
	return opens.index(open) == closes.index(close)

#Converting from decimal to binary
def divideby2(decNumber):
	remstack = Stack()
	
	while decNumber > 2:
		rem = decNumber % 2
		remstacl.push(rem)
		decNumber = decNumber // 2
	
	binString = ''
	while not remstack.isEmpty():
		binString = binString + str(remstack.pop())
		
	return binString

#Converting from decimal to any base
def baseConverter(decNumber, base):
	digits = '0123456789ABCDEF'
	remstack = Stack()
	while decNumber > 0:
		rem = decNumber % base
		remstack.push(rem)
		decNumber = decNumber // base
	
	newString = ''
	while not remstack.isEmpty():
		newString = newString + digits[remstack.pop()]
	
	return newString

#Palindrom Checker
def palChecker(aString):
	charDeque = Deque()
	
	for ch in aString:
		charDeque.addRear(ch)
		
	stillEqual = True
	
	while charDeque().size() > 1 and stillEqual:
		first = charDeque.removeFront()
		last = charDeque.removeRear()
		if first != last:
			return False
	
	return stillEqual

#Anagram Checker:
def anagram(s1, s2):
	s1 = s1.replace(' ','').lower()
	s2 = s2.replace(' ','').lower()
	
	return sorted(s1) == sorted(s2)

#Anagram Checker: Part 2
def anagram_checker(s1, s2):
	s1 = s1.replace(' ','').lower()
	s2 = s2.replace(' ' ,'').lower()
	
	if len(s1) != len(s2):
		return False
	
	count = {}
	for letter in s1:
		if letter in count:
			count[letter] += 1
		else:
			count[letter] = 1
	
	for letter in s2:
		if letter in count:
			count[letter] -= 1
		else:
			count [letter] = 1
	
	for k in count:
		if count[k] != 0:
			return False
	
	return True

	
		
