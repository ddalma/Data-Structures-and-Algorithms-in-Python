def BinaryTree(r):
	return [r, [],[]]

def insertLeft(root, new_branch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1, [new_branch, t,[]])
	else:
		root.insert(1, [new_branch, [],[]])
	
	return root

def insertRight(root, new_branch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2, [new_branch,[], t])
	else:
		root.insert(2, [new_branch, [] ,[]])
	return root

def getRootVal(root):
	return root[0]

def setRootVal(root, new_val):
	root[0] = new_val

def getLeftChild(root):
	return root[1]

def getRightChild(rrot):
	return root[2]


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
	
	def getRootVal(self):
		return self.key
	
	def setRootVal(self, obj):
		self.key = obj
	
	def getLeftChild(self):
		return self.leftChild
	
	def getRightChild(self):
		return self.rightChild




