def preorder(tree):
	print tree.getRootVal()
	preorder(tree.getLeftChild())
	preorder(tree.getRightChild())

def preorder(self):
	print self.key
	if self.leftChild:
		self.leftChild.preorder()
	if self.rightChild:
		self.rightChild.preorder()

def inorder(tree):
	inorder(tree.getLifeChild())
	print tree.getRootValue()
	inorder(tree.getRightChild())

def postorder(tree):
	postorder(tree.getLifeChild())
	postorder(tree.getRightChild())
	print tree.getRootVal()
	

def preorder(tree):
	print tree.getRootVal()
	preorder(tree.getLeftChild())
	preorder(tree.getRightChild())

def preorder(self):
	print self.key
	if self.leftChild:
		self.leftChild.preorder()
	if self.rightChild:
		self.rightChild.preorder()

def inorder(tree):
	preorder(tree.getLifeChild())
	print tree.getRootVal()
	preorder(tree.getRightChild())

def postorder(tree):
	postorder(tree.getLeftChild())
	postorder(tree.getRightChild())
	print tree.getRootVal()